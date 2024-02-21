---
id: 📙2d-linear-systems
aliases: []
tags:
  - "24-02-20"
title: 📙2-D Linear Systems
---

A **2-D linear system** is defined by the system 
$$
\begin{align*}
\dot{x}&=ax + by\\
\dot{y}&=cx + dy.\\
\end{align*}
$$
In matrix form, this is expressed as 
$$
\begin{align*}
\vec{x}&=\begin{bmatrix} x \\ y \end{bmatrix}
\dot{\vec{x}} &= A\vec{x} = \begin{bmatrix} a & b \\ c & d \end{bmatrix} \vec{x}.
\end{align*}
$$

In other words, both $\dot{x}$ and $\dot{y}$ are functions of $x$ and $y$. 

> [!example] Acceleration of a Spring
> 
> 1\. The motion of a spring is defined by the differential equation
> $$
> m\ddot{x}+kx=0
> $$
> where $m$ is the mass, $k$ is the spring constant, and $x$ is the displacement from the equilibrium position.
> 
> > [!summary]- Solution
> > 
> > Let $v=\dot{x}$, which represents the velocity of the spring. Then, we have 
> > $$
> > \dot{v}=-\frac k m x.
> > $$
> > If we graph the [[📕phase portraits|phase portrait]] (or $v$ as a function of $x$), the motion of a particle in the phase space is known as a **circular orbit**, where the particle orbits in a circle about the origin. In particular, this is known as a **closed orbit** because the motion eventuall returns to the starting point. As in this example, these systems arise mainly from oscillations. 
> > 
> > Suppose we took $\omega^2 = \frac k m$. Then, substituting, we get
> > $$
> > \frac{\dot{x}}{\dot{v}}=\frac{v}{-\omega^2 x}. 
> > $$
> > Cross multiplying and integrating, we get
> > $$
> > \omega^2\frac{x^2}{2} + \frac 1 2 v^2 = C.
> > $$
> > Notice that this function takes the form of an ellipse on the $x$-$v$ axis. 
> 
> 2\. Suppose we have the system 
> $$
> \dot{\vec{x}}=\begin{bmatrix} a & 0 \\ 0 & -1 \end{bmatrix} \vec{x}.
> $$
> Vizualize this system with a graph. 
> 
> > [!summary]- Solution 
> > 
> > First, we can solve to get $\dot{x}=ax$ and $\dot{y}=-y$, so $x(t)=x_0 e^{at}$ and $y(t)=y_G e^{-t}$. We can analyze the system for different $a$:
> > - For negative $a$, all initial solutions tend towards the origin. Furthermore, if $a< -1$, the trajectory will approach the $y$-axis faster than it will approach the $x$-axis. Here, we call $\vec{x}^*=0$ a [[📘attractors|stable node]]. 
> > - If $a=-1$, the path taken is a direct line. This formation is known as a **star**. 
> > - If $-1<a<0$, then the graph instead curves towards the $x$-axis. 
> > - If $a=0$, then solutions move down in $y$ but stay constant in $x$. The [[📘equilibrium points|fixed points]] are arranged along the line $y=0$. 
> > - Finally, in the case where $a>0$, the solutions tend towards $y=0$ and $x=\pm \infty$, depending on the initial sign of $x$. If we start on the $y$-axis, the solution tends towards an [[📘repellers|unstable equilibrum point]] at $(0,0)$. 
> > 
> > In the final case, the $y$-axis is a [[📘stable manifold|stable manifold]] and the $x$-axis is an [[📘unstable manifold|unstable manifold]].Note that the point $(0,0)$ is actually a [[📘liapunov stable|Liapunov stable point]].

