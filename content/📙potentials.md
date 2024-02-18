---
id: 📙potentials
aliases:
  - 📙potential
tags:
  - "24-01-29"
title: 📙Potentials
---

Potentials are a method of visualizing dynamics. Suppose we have a [[📘order|1st-order]] differential equation given by $\dot{x}=f(x)$, where $f(x)$ is defined as 
$$
f(x)=-\frac{dV}{dx}
$$
where $V(x)$ is the potential function. Expanding by the chain rule, we have 
$$
\begin{align*}
\frac{dV}{dt}&=\frac{dV}{dx}\cdot \frac{dx}{dt}\\
&=-\left(\frac{dV}{dx}\right)^2.\\
\end{align*}
$$
In particular, if the particle is in equilibrium, $f(x)=\frac{dV}{dx}=0$, so $V(x)$ is a constant. If $V(x)$ is local minima, than the point is an [[📘attractor|attractor]]; if $V(x)$ is a local maxima, than the point is a [[📘repeller|repeller]].

> [!example] Finding Equilibrium Points with Potentials
>
> 1. Find $V(x)$ for $\dot{x}=-x$
>
> > [!summary]- Solution
> > 
> > $V(x)=\frac 1 2 x^2+C$
> 
> 2. Find $V(x)$ for $\dot{x}=x-x^3$
> 
> > [!summary]- Solution 
> > 
> > $V(x)=-x^2+x^4$
