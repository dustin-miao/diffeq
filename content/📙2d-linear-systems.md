---
id: 📙2d-linear-systems
aliases: []
tags:
  - "24-02-20"
  - "24-02-22"
title: 📙2-D Linear Systems
---

### Definition

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

### Classification of Linear Systems

In solving 2-D linear systems, it helps to identify straight line trajectories. We can extrapolate these solutions to the general case by taking a linear combination. Along the straight line, the solution will be exponential. Specifically, the solution will take the form 
$$
\vec{x}(t)=e^{\lambda t} \cdot \vec{v}
$$
where $\vec{v}$ represents the line spanned by the vector. We get that 
$$
\dot{\vec{x}}=\lambda e^{\lambda t}\cdot \vec{v}.
$$
Recall that a solution of the system must satisfy 
$$
\dot{\vec{x}}=A\vec{x},
$$
so we get 
$$
\lambda \vec{v}=A\vec{v}.
$$
Thus, $\vec{v}$ is the [[📘eigenvectors|eigenvector]] of $A$, and $\lambda$ is the associated **eigenvalue**. To solve this system

> [!example] Classification of Linear Systems 
> 
> 1\. Find the equilibrium solutions of the system described by $\dot{x}=x+y$ and $\dot{y}=4x-2y$. 
> 
> > [!summary]- Solution
> > 
> > First, we express the system in matrix form:
> > $$
> > \dot{\begin{bmatrix} x \\ y \end{bmatrix}} = \begin{bmatrix} 1 & 1 \\ 4 & -2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix}.
> > $$
> >
> > Expressing in the form $A-2\lambda I$, we have 
> > $$
> > \begin{bmatrix} 1 & 1 \\ 4 & -2 \end{bmatrix} - \begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix} = \begin{bmatrix} 1 -\lambda & 1 \\ 4 & -2-\lambda \end{bmatrix}.
> > $$
> > Taking the [[📘determinant|determinant]], we get that 
> > $$
> > (1-\lambda)(-2-\lambda)-4= 0,
> > $$
> > so $\lambda_1 = 2$ and $\lambda_2 = -3$. Substituting $\lambda_1$ into $A-\lambda I$, we get the equation 
> > $$
> > \begin{bmatrix} -1 & 1 \\ 4 & -4 \end{bmatrix} \begin{bmatrix} v_a \\ v_b \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.
> > $$
> > The two non-trivial solutions for $\lambda_1$ and $\lambda_2$ are $\langle 1, 1\rangle$ and $\langle 1, -4\rangle$. 
The general solution is given by a linear combination of the specific cases, so the solution is 
> > $$
> > \vec{x}(t)=C_1 \begin{bmatrix} 1 \\ 1 \end{bmatrix} e ^{2t} + C_2\begin{bmatrix} 1 \\ -4 \end{bmatrix} e^{-3t}.
> > $$
> > 
> > To get the closed form solution for an [[📘initial value problem|initial value problem]], we need to solve a system of equation in terms of $C_1$ and $C_2$. 
> > 
> > The phase plot is given by
> > ![[2d-phase-plot-example.png]]
> > The origin, in this case, is known as a **saddle**. The [[📘stable manifold|stable manifold]] is given by $\langle 1, -4 \rangle$ and the [[📘unstable manifold|unstable manifold]] is given by $\langle 1, 1 \rangle$. We can get this by examining the sign of the eigenvalues. 
> 
> 2\. Sketch a typical phase portrait for $\lambda_2 < \lambda_1 < 0$. 

In the general case, we have
$$
\det(A - \lambda I) = \det\begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = (a-\lambda)(d-\lambda) - bc = 0.
$$
Define $\text{trace}(A) = \tau$ and $\det(A) = \Delta$. Then, expanding and solving for $\lambda$, we get 
$$
\lambda = \frac{\tau \pm \sqrt{\tau^2 - 4\Delta}}{2}.
$$
In particular, when $\tau^2-4\Delta < 0$, then we will get complex eigenvalues. Let $\lambda=\alpha \pm j\beta$. 


