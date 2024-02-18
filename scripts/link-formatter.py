import os
import re

with open("content-path.txt", "r") as content_path_file:
  content_path = content_path_file.readline().rstrip()
  assert os.path.exists(content_path)

all_files = []
for root, dirs, files in os.walk(content_path):
  for file in files: 
    all_files.append(os.path.join(root, file))

file_regex = re.compile(r"[📕📘📗📙🗒️]?[a-z ]+\.md")
content_files = sorted([file for file in all_files if file_regex.search(file)])
print("content_files = {")
for file in content_files:
  print(f"\t\"{file}\"")
print("}")

link_regex_reg = re.compile(r"\[\[[📕📘📗📙🗒️][a-z ]+\]\]")
link_regex_sub = re.compile(r"\[\[[📕📘📗📙🗒️][a-z ]+\|[📕📘📗📙🗒️][a-zA-Z0-9 \-]+\]\]")
for file in content_files:
  with open(file, "r") as file: 
    content = file.read()
  content = re.sub(link_regex_reg, lambda match: match.group(0)[:-2] + f"|{match.group(0)[3:-2]}]]", content)
  content = re.sub(link_regex_sub, lambda match: match.group(0)[:match.group(0).index("|") + 1] + match.group(0)[match.group(0).index("|") + 2:], content)
  # print(content)
  with open(file.name, "w") as file:
    file.write(content)
