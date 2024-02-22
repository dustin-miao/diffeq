---
id: 📘eigenvectors
aliases: []
tags:
  - "24-02-22"
title: 📘Eigenvectors
---

An **eigenvector** for a matrix $A$ is defined as any $\vec{v}$ that satisfies 
$$
A\vec{v}=\lambda \vec{v}
$$
for some scalar $\lambda$. In other words, $\vec{v}$ is scaled by some constant by the linear transformation described by $A$. Such a vector exists if and only if 
$$
\det(A-\lambda I) = 0.
$$
We can solve by first taking the [[📘determinant|determinant]] and finding all **eigenvalues** $\lambda$, then substituting and solving for $(A-\lambda I)\cdot \vec{v}=\vec{0}$. Note that $\langle 0, 0\rangle$ is always a trivial solution.
