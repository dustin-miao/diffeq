---
id: 📙limit cycles
aliases: []
tags:
  - "24-03-19"
  - "24-03-21"
title: 📙Limit Cycles
---

A **limit cycle** is an isolated closed-trajectory that is attracting/stable. 

For instance, take the system 
$$
\begin{align*} \dot{r}&=r(1-r^2)\\\dot{\theta}=1 \end{align*}.
$$
Because the two variables are decoupled, we can examine the two variables seperately. Assuming that $r$ is positive, the [[📕phase portraits|phase portrait]] is a parabola with intercepts at $r=0$ and $r=1$. In particular, the solution at $r=1$ is [[[[📘attractors|attracting]]. Thus, because $\dot{\theta}$ is constantly changing with respect to time, the [[📕phase portraits|phase portrtait]] takes the form of a circle of radius $1$ that attracts all points around it.

Note that limit cycles can also be [[📘repellers|unstable]]: paths outside of the limit cycle can go to infinity, and paths inside can go to $0$. 

The most notable example of a limit cycle is a **van der Pol oscillator**, which is dictated by 
$$
\ddot{x}+\mu(x^2-1)\dot{x}+x= 0
$$
where $\mu\geq 0$ is a positive constant. It can be shown that the function converges to a limit cycle for every value of $\mu$, but we will focus on the specific case of $\mu=1.5$. The phase portrait can be visualized in Mathematica:

``
StreamPlot[{y, -1.5 (x^2 - 1) y - x}, {x, -5, 5}, {y, -7, 7}, 
 Axes -> True]
```
