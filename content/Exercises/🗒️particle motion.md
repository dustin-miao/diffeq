---
id: 🗒️particle motion
aliases: []
tags:
  - "24-01-29"
title: 🗒️Particle Motion
---

Suppose there is a partical that travels on the half-line ($x\geq 0$) with $\dot{x}=-x^c$, where $c$ is a real constantSuppose there is a partical that travels on the half-line ($x\geq 0$) with $\dot{x}=-x^c$, where $c$ is a real constant.
1. Find all values of $c$ such that the origin is a [[📘stable]] [[📘fixed point]].
2. Assume $c$ is chosen such that $x=0$ is [[📘stable]]. How long does it take for the particle to go from $x=1$ to $x=0$ as a function of $c$?

> [!summary]- Solution
>
> 1\. Since $x\geq 0$, $\dot{x}$ is always negative, so the origin is always a stable fixed point.
> 
> 2\. We get the solution of the DE is 
> $$
> \frac{-x^{-c_0+1}}{-c_0+1}=t+c_1.
> $$
> Solving for $x$, we find $t$ when $x=0$, which yields
> $$
> t=\frac{-x_0^{1-c_0}}{c_0-1}
> $$
> which is only valid when $c_0<1$. The final answer is given by 
> $$
> t=\frac 1 {1-c_0}.
> $$
