---
id: 📙higher order linear systems
aliases: []
tags:
  - "24-04-11"
  - "24-04-15"
  - "24-04-17"
title: 📙Higher Order Linear Systems
---

### General Higher-Order Linear Systems

Suppose we are given the linear system $\dot{\vec{x}}=A\vec{x}$, where 
$$
A = \begin{bmatrix} 1 & 2 & -1 \\ 0 & 3 & -2 \\ 0 & 2 & -2 \end{bmatrix}.
$$

We can find the eigenvalues by setting $\det(A-\lambda I)=0$, which yields $\lambda=1,2,-1$. Using standard methods, we find the eigenvectors to be $\langle 3, 2, 1\rangle$, $\langle 1, 0, 0\rangle$, $\langle 0, 1, 2\rangle$, respectively. Thus, our transformation matrix to the eigenbasis is given by 
$$
T = \begin{bmatrix} 3 & 1 & 0 \\ 2 & 0 & 1 \\ 1 & 0 & 2 \end{bmatrix}.
$$

Note that the multiplication $T^{-1}AT$ is a diagonal matrix with the eigenvectors, which makes the solution to the linear system easy to find: $y_1(t)=C_1e^{2t}$, $y_2(t)=C_2e^{t}$, and $y_3(t)=C_3e^{-t}$. The general solution in the normal basis is simply given by 
$$
\vec{x}(t)=T\cdot \vec{y}.
$$

In a 3-dimensional system, if $\lambda_3<\lambda_2<\lambda_1<0$, then all trajectories will tend to the origin, forming a higher-dimensional sink. In this system, any trajectory will approach $0$ tangent to the axis corresponding to $\lambda_1$. 

### Complex Eigenvalues

Consider a general linear system $\dot{\vec{x}}=A\vec{x}$ such that $A$ has distinct eigenvalues $\lambda_1, \lambda_2, \dots, \lambda_{k_1}\in \mathbb{R}$ and $\alpha_1\pm j\beta_1, \alpha_\pm j\beta_2, \dots, \alpha_{k_2}\pm j\beta_{k_2} \in \mathbb{C}$. Now, the matrix $T^{-1}AT$ takes on the form 
$$
T^{-1}AT=\begin{bmatrix} \lambda_1 \\ & \lambda_2 \\ & & \ddots \\ & & & \lambda_{k_1} \\ & & & & \alpha_1 & \beta_1 \\ & & & & -\beta_1 & \alpha_1  \\ & & & & & & \alpha_2 & \beta_2 \\ & & & & & & -\beta_2 & \alpha_2 \\ & & & & & & & & \ddots \\ & & & & & & & & & \alpha_{k_2} & \beta_{k_2} \\ & & & & & & & & & -\beta_{k_2} & \alpha_{k_2}\end{bmatrix}.
$$
Recall that the solution in the eigenspace takes the form of $C_ne^{\lambda_nt}$ for eigenvalue $\lambda_n$ and 
$$
\begin{bmatrix}
a_n e^{\alpha_n t}\cos \beta_n t + b_ne^{\alpha_nt}\sin \beta_n t \\
-a_n e^{\alpha_n t}\sin \beta_n t + b_n e^{\alpha_n t}\cos \beta_n t
\end{bmatrix}
$$
for eigenvalue $\alpha_n + j\beta_n$. To compute the $T$ matrix, note that we only have to compute one of each conjugate pair of eigenvalues/eigenvectors. Then, we decompose each complex eigenvector into its real and imaginary components, which we treat as the new eigenbasis for that conjugate pair. In the end, our $T$ matrix remains a $n\times n$ matrix.  

> [!example] A Complex Linear System 
> 
> Solve the linear system given by 
> $$
> \dot{\vec{x}}=\begin{bmatrix} 0 & 1 & 0 \\ -1 & 0 & 0 \\ 0 & 0 & -1 \end{bmatrix} \vec{x}.
> $$

### Repeated Eigenvalues

Suppose we have a system with 3 repeated eigenvalues, corresponding to solution $x(t)$, $y(t)$, and $z(t)$. The three solutions are given by 
$$
\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} C_1e^{\lambda t} + C_2 t e^{\lambda t} + C_3 t^2e^{\lambda t} \\ C_2e^{\lambda t} + C_3 t e^{\lambda t} \\ C_3 e^{\lambda t} \end{bmatrix}.
$$
However, this is not the only possible form of the solution. Another possibility includes
$$
\begin{bmatrix} x \\ y \\ z \end{bmatrix}=\begin{bmatrix}C_1e^{\lambda t} + C_2 te^{\lambda t} \\ C_2e^{\lambda t} \\ C_3 e^{\lambda t} \end{bmatrix}.
$$

In practice, the probability of 3 or more eigenvalues coinciding is extremely low. 

### Another Approach to Higher-Order Systems

Our current approach relies on decomposing $n$-th order equations into first and second order, and combining the solutions using the eigenbasis. 

Our new approach will instead compute the "exponential" of the $A$ matrix. Recall that for a number $a$, $e^a$ can be defined in one of the following two ways:
$$
\lim_{n\to\infty} \left( 1 + \frac a n \right )^n \\ 
e^a = \sum_{n=0}^\infty \frac{a^n}{n!}
$$

By analogy, we define the exponential of a square matrix $A$ in a similar way: 
$$
\lim_{n\to\infty} \left( I + \frac 1 n A \right )^n \\ 
e^a = \sum_{n=0}^\infty \frac{A^n}{n!}
$$

where $I$ denotes the identity matrix with the same dimension as $A$. For convenience, we define $A^0=I$. 

Recall that the soution for the differential equation $x'=ax$ is given by $x(t)=Ce^{at}$, where $C=x(0)$. By analogy, if $\dot{\vec{x}}=A\vec{x}$, then $\vec{x}(t)=e^{tA}\cdot \vec{c}$, where $\vec{c}=\vec{x}(0)$. 

To show that this is true, suppose we know that the solution is of the form $\vec{x}(t)=e^{tA}\cdot \vec{c}$. We know that 
$$
\begin{align*}
\frac{d}{dt}\vec{x}(t)&=\frac{\vec{x}(t+\Delta t)-\vec{x}(t)}{\Delta t}\\
&=\frac{e^{(t+\Delta t)A}\cdot \vec{c}-e^{tA}\cdot \vec{c}}{\Delta t}\\
&= \frac{\left(e^{\Delta t\cdot A}-I\right)\cdot e^{tA}\cdot \vec{c}}{\Delta t}
\end{align*}
$$
By definition, we know that $\vec{x}(t)=e^{tA}\cdot \vec{c}$, so what is left is to reduce the other term.
$$
\begin{align*}
\frac{e^{\Delta t\cdot A}-I}{\Delta t}&= \frac{I + \Delta t A + \frac 1 {2!}(\Delta t A)^2 + \frac 1 {3!}(\Delta tA)^3 + \cdots-I}{\Delta t} \\
&= \frac{I+\Delta tA - I}{\Delta t}\\
&= A
\end{align*}
$$

If we do not know the form of the solution, instead consider the following where a particle is located at some point $\vec{x}(0)$ and we need to find its position after some short time $t=\Delta t$ which is given by $\vec{x}(\Delta t)$. 
$$
\begin{align*}
\dot{\vec{x}}&=A\vec{x}\\
\frac{\vec{x}(\Delta t)-\vec{x}(0)}{\Delta t}&=A\cdot\vec{x}(0)\\
\vec{x}(\Delta t) &= \vec{x}(0)+\Delta t\cdot A\vec{x}(0)\\
&=(I+\Delta t\cdot A)\vec{x}(0)
\end{align*}
$$
Applying the same logic, at time $2\Delta t$, the particle will be at $\vec{x}(2\Delta t)=(I+\Delta tA)\vec{x}(\Delta t)=(I+\Delta tA)^2\vec{x}(0)$. In general, we get that 
$$
\vec{x}(N\Delta t)=(I+\Delta tA)^N\vec{x}(0)
$$
In the limit $\Delta t=\frac N t \to 0$, we get that $\vec{x}(t)=(I+\frac{t}{N}A)^N \vec{x}(0)=e^{At}\vec{x}(0)$. 

### Affine Systems

An affine system is given by the expression $\dot{\vec{x}}=A\vec{x}+\vec{f}(x)$ for some constant vector $\vec{f}$. To solve, we find the homogeneous solution using methods described above, and find the particular solution based on $\vec{f}$. 

> [!example]
> 
> Find the particular solution to 
> $$
> \dddot{x}+4\ddot{x}-7\dot{x}-10x=100t^2-64e^{3t}
> $$
> for $x(0)=-20$, $\dot{x}(0)=\frac{-29}{5}$, $\ddot{x}=\frac{19}{5}$. 
