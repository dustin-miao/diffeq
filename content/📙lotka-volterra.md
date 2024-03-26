---
id: 📙lotka-volterra
aliases: []
tags:
  - "24-03-13"
  - "24-03-19"
title: 📙Lotka-Volterra Systems
---

The **Lotka-Volterra systems** model systems that face competition for resources. Consider the following example:
$$
\begin{align*}
\dot{x}=x(3-x-2y)\\
\dot{y}=y(2-x-y)
\end{align*}
$$
where $x(t)$ is the population of $A$ and $y(t)$ is the population of $B$. We can visualize this using methods described in [[📙2d-nonlinear-systems]]. We find equilibrium points at $(0,0)$, $(1,1)$, $(3,0)$, and $(0,2)$.

Now, consider the system described by $x(t)$, or the size of the prey population, and $y(t)$, or the size of the predator population. 
$$
\begin{align*} \dot{x} &= \alpha x - \xeta x y \\ \dot{y}=\delta x y - \gamma y \end{align*}.
$$
This model assumes that the enivornment stays constant, the prey has an ample food supply, and that the predators food supply depends entirely on the prey. The nullclines are given by $x=\gamma / \delta$ and $y=\alpha/\beta$. 
[[!lotka-volterra-predator-prey-example.png]]
 
Because each solution is closed, some quantity must be conserved. We get that 
$$
\frac{dy}{dx}=\frac{\delta x y - \gamma y}{\alpha x - \beta xy}.
$$
This system is seperable, so we get 
$$
\frac{(\alpha - \beta y)dy}{y}=\frac{(\delta x - \gamma)dx}{x}.
$$
Integrating on both sides, we get that 
$$
V(x,y)=\delta x - \gamma \ln x + \beta y - \alpha \ln y.
$$
