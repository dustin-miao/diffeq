---
id: 📙2d-linear-systems
aliases: []
tags:
  - "24-02-20"
  - "24-02-22"
  - "24-02-26"
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

### Complex Eigenvalues

In the general case, we have
$$
\det(A - \lambda I) = \det\begin{bmatrix} a - \lambda & b \\ c & d - \lambda \end{bmatrix} = (a-\lambda)(d-\lambda) - bc = 0.
$$

Define $\text{trace}(A) = \tau$ and $\det(A) = \Delta$. Then, expanding and solving for $\lambda$, we get 
$$
\lambda = \frac{\tau \pm \sqrt{\tau^2 - 4\Delta}}{2}.
$$
In particular, when $\tau^2-4\Delta < 0$, then we will get complex eigenvalues. Let $\lambda_{1,2}=\alpha \pm j\beta$. The associated [[📘eigenvectors|eigenvectors]] will also be complex, which we will again denote as $\vec{v_1}$ and $\vec{v_2}$. The general solution still takes the form  
$$
\vec{x}(t)=C_1 e^{\lambda_1 t}\cdot \vec{v_1} + C_2 e^{\lambda_2 t} \cdot \vec{v_2}.
$$

Expanding using Euler's formula, we get that $\vec{x}(t)$ is a linear combination of $e^{\alpha t}\cos \beta t$ and $e^{\alpha t}\sin \beta t$. If $\alpha=0$, then $e^{\alpha t}=0$ for all time and the [[📕phase portraits|phase portrait]] is simply a circle. Otherwise, it takes the form of a spiral, going either in or out depending on the sign of $\alpha=\text{Re}(\lambda)$. A **decaying oscillation**, whene $\alpha< 0$, is known as a **stable spiral**, whereas a **growing oscillation** is known as an **unstable spiral**. 

From a high level, we can generalize this method by defining $z(t)=x(t)+jy(t)$. Suppose we are given a system of the form:
$$
\dot{\begin{bmatrix} x \\ y \end{bmatrix}}=\begin{bmatrix} \alpha & \beta \\ -\beta & \alpha \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix}.
$$
Then, we have 
$$
\begin{align*}
\dot{z}(t)&=\dot{x}(t)+j\dot{y}(t) \\ 
&=(\alpha x+\beta y)+j(-\beta x+\alpha y) \\
&=\alpha(x+jy)-j\beta(x+jy) \\
&= (\alpha - j\beta)z.
\end{align*}
$$

So $\dot{z}(t) = \gamma z$. From before, we know that the solution to this system is $z(t)=e^{\gamma t}\cdot C$, where $C$ may be complex. We can express this as 
$$
\begin{align*}
x(t)+jy(t)&=(C_1+jC_2)e^{(\alpha-j\beta)t}\\
&= C_1e^{\alpha t}\cos \beta t + C_2e^{\alpha t}\sin \beta t + j(C_2e^{\alpha t}\cos \beta t - C_1 e^{\alpha t}\sin \beta t).
\end{align*}
$$

This shows that both $x(t)$ and $y(t)$ are real, despite having complex eigenvalues. Also, note that this method does not find the [[📘eigenvectors|eigenvectors]].

Consider the system given by $\dot{x}=x-y$ and $\dot{x}=x+y$. Solving using methods above, we get that $x(t)=C_1e^t\cos t - C_2e^t \sin t$ and $y(t)=C_2e^t\cos t + c_1e^t\sin t$. Alternatively, we can find the eigenvalues $\lambda=1\pm j$ and the corresponding [[📘eigenvectors|eigenvectors]] $v_1=\langle i,1\rangle$ and $v_2=\langle -i,1\rangle$. 

Notice that because $\lambda_1$ and $\lambda_2$ are complex conjugates, each component of $v_1$ and $v_2$ are complex conjugates as well. Furthermore, because $x(t)$ and $y(t)$ are real, as shown above, $C_1$ and $C_2$ are also complex conjugates. Expanding and simplfying using algebra, we get 
$$
\vec{x}(t)=e^t (C_1+C_2)\begin{bmatrix}-\sin t \\ \cos t\end{bmatrix}+j(C_1-C_2G)e^t\begin{bmatrix} \cos t \\ \sin t \end{bmatrix}.
$$

### Repeated Eigenvalues 

If the two eigenvalues are the same, there are two cases:
1. 2 eigenvectors correspond to $\lambda$
2. 1 eigenvector corresponds to $\lambda$

In the first place, the eigenvectors span the plane (i.e. every point on the plane is a linear combination of the vectors). This implies that every vector is an eigenvector (consider $\vec{x_0}=c_1\vec{v_1}+ c_2\vec{v_2}$ and solving for $A\vec{x_0}$). Then, $A$ must take the form 
$$
A=\begin{bmatrix} \lambda & 0 \\ 0 & \lambda \end{bmatrix}.
$$
The solution must look like $\vec{x}(t)=e^{\lambda t}\cdot \vec{x_0}$. The [[📕phase portrait|phase portrait]] takes the form of a **star** centerd at the origin. If $\lambda=0$, then the plane is full of fixed points. 

In the second case, all trajectories will approach the eigenvector in one direction. This case is known as a **degenerate node**. For the intuition on what the [[📕phase portrait|phase portrait]] looks like, consider two eigenvectors with negative eigenvalues. One of these will be "fast", and the other will be "slow", and trajectories will approach along the slow side. The single eigenvector case occurs when the two eigenvectors approach each other. 

### General Case 

Consider the general form 
$$
\lambda=\frac{\tau \pm \sqrt{\tau^2 - 4\Delta}{2}}.
$$

Then, we can categorize the origin based on values of $\tau$ and $\Delta$. 


![[img/2d-linear-system-categorization.png]]

Consider the following 8 canonical forms of the $A$:

1. $\begin{bmatrix} \lambda_1 & 0 \\ 0 & \lambda_2 \end{bmatrix}$ for $\lambda_1, \lambda_2 < 0$, $\lambda_1, \lambda_2 > 0$ and $\lambda_1<0,\lambda_2 > 0$. 
2. $\begin{bmatrix} \alpha & \beta \\ -\beta & \alpha \end{bmatrix}$ for $\alpha<0,\beta\neq 0$, $\alpha>0,\beta\neq 0$, and $\alpha=0,\beta\neq 0$. 
3. $\begin{bmatrix} \lambda & 1 \\ 0 & \lambda \end{bmatrix}$ for $\lambda < 0$ and $\lambda > 0$ 


The solutions are given by:
1. $\vec{x}(t)=C_1e^{\lambda_1 t}\vec{v_1} + C_2e^{\lambda_2 t} \vec{v_2}$
2. See [[📙2d-linear-systems#Complex Eigenvalues]]
3. See Homework Exercise 5.1.11

In general, we would like to perform a change of basis to transform a general matrix into one of these forms. 
