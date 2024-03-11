---
id: 📙nonlinear-2nd-order-systems
aliases: []
tags:
  - "24-03-05"
title: 📙Nonlinear 2nd-Order Differential Equations
---

Because most nonlinear systems do not have a closed form solution, we will focus mainly on the qualitative behavior of systems. 

> [!example] A simple Nonlinear System
> 
> Graph the following system given by $\dot{x}=x-e^{-y}$ and $\dot{y}=-y$.
>
> > [!summary]- Solution 
> > 
> > First, we try to identify equilibrum points, where $\dot{x}=\dot{y}=0$. We get this value to be $(-1,0)$. 
> > 
> > Secondly, we want to find **nullclines**, or where $\dot{x}=0$ or $\dot{y}$. Along these nullclines, the flow is completely horizontal or completely vertical. Solving, we get that the vectors are vertical along the graph $x=-e^{-y}$ and $y=0$. Note that to find the direction (left/right or up/down), we need to analyze the differential equation itself. At this point, we can categorize the fixed point as a nonlivnear version of a [[📙2d-linear-systems|saddle]].
> > 
> > Then, we categorize each region based on the signs of $\dot{x}$ and $\dot{y}$. We find that on the top-left, $\dot{x}<0$ and $\dot{y}<0$; on the top-right, we have $\dot{x}>0$ and $\dot{y}<0$; on the bottom-left, above the line $x=-e^{-y}, we have $\dot{x}<0$ and $\dot{y}>0$; and on the bottom right, we have $\dot{x}>0$ and $\dot{y}>0$. 
> > 
> > Graphing, we find that the graph matches our predictions:
> > ![[img/2d-nonlinear-example-1.png]]
> 
> Graph the following system given by $\dot{x}=x-x^3$ and $\dot{y}=-y$.
> 
> > [!summary]- Solution 
> > 
> > The nullclines are given by $x(x-1)(x+1)=0$ and $y=0$. We can solve for each of the eight regions (2 regions, by symmetry), which yields the following diagram. 
> > 
> > ![[img/2d-nonlinear-example-2.png]]

### Fixed Points and Linearization

Wec an approximate a phase portrait near a fixed point by linearizing it and using techniques from solving [[📙2d-linear-systems|linear systems]]. Suppose we have some system 
$$
\begin{align*}
\dot{x}&=f(x,y)\\
\dot{y}&=g(x,y)
\end{align*}
$$

Suppose there is some fixed point at $(x^*, y^*)$, implying that $f(x^*,y^*)=g(x^*,y^*)=0$. Let $u=x-x^*$ and $v=y-y^*$. Then, we have 
$$
\begin{align*}
\dot{u}=\dot{x}&=f(x^*+u,y^*+v)\\
&= f(x^*,y^*)+u\frac{\partial f}{\partial x}+v\frac{\partial f}{\partial y}+\mathcal{O}(u^2,v^2,uv)
\end{align*}
$$

In other words, we have 
$$
\dot{u}=u\frac{\partial f}{\partial x}+v\frac{\partial f}{\partial y},
$$
so $\dot{u}$ is linear in $u$ and $v$. Repeating for $v$, we get 
$$
\dot{v}=u\frac{\partial g}{\partial x}+v\frac{\partial g}{\partial y}.
$$

In other words, we have 
$$
\dot{\begin{bmatrix} u \\ v \end{bmatrix}} = \begin{bmatrix} \frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} \\ \frac{\partial g}{\partial x} & \frac{\partial g}{\partial y} \end{bmatrix} \begin{bmatrix} u \\ v \end{bmatrix}.
$$
Near the point, the behavior of the system is categonized by this system of differential equations. This matrix is known as the **Jacobian**. 

> [!example] Analyzing Fixed Points through Linearization 
> 
> 1\. Find the fixed points and classify them using linearization for the following system: 
> $$
> \begin{align*}
> \dot{x}&=-x+x^3\\
> \dot{y}&=-2y 
> \end{align*}
> $$
> > [!summary]- Solution 
> > 
> > We get the $A$ matrix as 
> > $$
> > \begin{\bmatrix} -1+3x^2 & 0 \\ 0 & -2 \end{bmatrix}. 
> > $$
> > Plugging in for each of $(x^*,y^*)=(0,0),(-1,0),(1,0)$, we get that the points are stable, saddle, and saddle, respectively. 
> 
> 2\. Classify the fixed point $(0,0)$ for the following system:
> $$
> \begin{align*}
> \dot{x}&=-y+ax(x^2+y^2) \\
> \dot{y}&=x+ay(x^2+y^2)
> \end{align*}
> $$
