---
id: 📙higher order linear systems
aliases: []
tags:
  - "24-04-11"
  - "24-04-15"
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
a_n e^{\alpha_n t}\cos \beta_n t + b_ne^{\alpha_nt}\sin \beta_1 t \\
-a_n e^{\alpha_n t}\sin \beta_n t + b_1 e^{\alpha_n t}\cos \beta_n t
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

Our current approach relies on decomposing $n$-th order equations into first and second order, and combining the solutions using the eigenbasis. Our new approach will instead compute the "exponential" of the $A$ matrix. 
