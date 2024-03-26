---
id: 📙2d nonlinear systems
aliases: []
tags:
  - "24-03-05"
  - "24-03-11"
title: 📙2-D Nonlinear Systems
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

### Tools to Analyze Second Order Systems 

Suppose a system can be written in the form $\dot{x}=-\nabla V$ for some continuous, differentiable, scalar function $V(\vec{x})$. This is known as a gradient systems with potential function $V(\vec{x})$. 

**Theorem**: Closed orbits are imposible in gradient systems. 
_Proof_: Suppose there was a closed orbit. Consider $\delta V$ after $1$ loop. Since $V$ is a scalar function, $\delta V = 0$. On the other hand, 
$$
\delta V = \int_0^T \frac{dV}{dt} dt=\int_0^T(\nabla V\cdot \dot{\vec{x}})dt=-\int_0^T \lvert\lvert \dot{\vec{x}}\rvert\rvert^2 dt.  
$$
This leads to a contradiction.

Thus, to show that there are no closed orbits in a system, we need to show that there exists a $V(x,y)$ such that $V_x=\dot{x}$ and $V_y=\dot{y}$. For example, consider $\ddot{x}+\dot{x}^3+x=0 and show that there are no periodic solutions. 

We can use a proof by contridiction. Set $E(x,\dot{x})=\frac 1 2 (x^2+\dot{x}^2)$. We know that $\Delta E = 0$ around a closed orbit. However, $\Delta E = \int_0^T \dot{E} dt$. We have $\dot{E}=x\dot{x}+\dot{x}\ddot{x}=-\dot{x}^4<0$. Since $T>0$, this leads to a contradiction. 
