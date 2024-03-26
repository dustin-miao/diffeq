---
id: 📗poincare-bendixson theorem
aliases: []
tags:
  - "24-03-21"
  - "24-03-25"
title: 📗Poincare-Bendixson Theorem
---

The Poincare-Bendixson Theorem described the long-term behavior of second order dynamical systems. To motivate this, we return to [[📘order|1st-order]] dynamical systems:

Recall that for $x'=\alpha x$, any initial condition settles to the fixed point at $x=0$. For $\alpha>0$, any trajectory that starts outside of the fixed point shoots off to infinity. For the equation $x'=\alpha x(1-x)$, $x=0$ tends to zero and all other trajectories settle at the fixe point $x=1$. Thus, we can extrapolate that any first order system will exhibit only 2 kinds of long term behavior: approaching a fixed point or shooting off to infinity.

In the 2-D case, there are more cases to analyze. If the equation is linear, we can break it down into one of the 8 canonical forms, as described in [[📙2d linear systems]]. We find that there is three possibilities: approaching a fixed point, shooting off to infinity, or following a cycle (in the case where it takes the form of a center, i.e. $\dot{x}=\alpha x+\beta y$ and $\dot{y}=-\beta x +\alpha y$).

For non-linear equations, we will analyze four cases: 

The first case is [[📙lotka-volterra|Lotka-Volterra]] systems, described by equations
$$
\dot{\begin{bmatrix}x\\y\end{bmatrix}}=\begin{bmatrix}(\alpha-\beta y)x \\ -(\gamma-\delta x)y\end{bmatrix},
$$
which follows a cyclical path, unless it starts at $(0,0)$.

The second case is [[📙limit cycles|var der Pol oscillators]], described by 
$$
\dot{\begin{bmatrix}x\\y\end{bmatrix}}=\begin{bmatrix}y\\\mu(1-x^2)y-x\end{bmatrix},
$$
which converges to a limit cycle.

Finally, we have a [[📙conservative systems|perdulum systems]], given by 
$$
\dot{\begin{bmatrix}\theta \\ \omega\end{bmatrix}} = \begin{bmatrix} \omega \\ - \frac g l \sin \theta \end{bmatrix},
$$
which forms a heteroclinic cycle, or a cycles that allow access to other cycles via. saddle nodes. These solutions constitute the **Poincare-Bendixson set**. Formally, any second order differential equation will exhibit one of three kinds of long term behavior: go to infinity, go to a fixed point, or go along a cycle (which can be neutral, limit, or heteroclinic). 

![[img/poincare-bendixson.png]]

Suppose we are given the system 
$$
\dot{r}=r(1-r^2)+\mu r \cos \theta
$$
where $\dot{\theta} = 1$. We know how to solve the system for $\mu=0$. To show that a similar closed loop exists for $\mu>0$, we want to find an $r_\text{min}$ and an $r_\text{max}$ such that $\dot{r}<0$ on the outer circle and $\dot{r}>0$ on the inner circle. Because $\dot{\theta}\neq 0$, there are no fixed points. 

Then, because $\cos\theta \geq -1$ for all $\theta$, for $\dot{r}>0$ we have $(1-r^2)-\mu > 0$, so $r_\text{min}<\sqrt{1-\mu}$ (we will say that $r_\text{min}<0.99\sqrt{1-\mu}$). Using a similar derivation, we can also get that $r_\text{max}>1.01\sqrt{1+\mu}$. The inclosed region is known as the **trapping region**.  

As another example, we are given the system 
$$
\begin{align*}
\dot{x}&=-x+ay+x^2y \\
\dot{y}&=b-ay-x^2y 
\end{align*}
$$
where $x$ is the concentration of ADP and $y$ is the concentration of F6P. This system models the process of glycolysis. 

The two nullclines are given by $y=\frac{x}{a+x^2}$ and the other is $y=\frac{b}{a+x^2}$. Consider $\dot{x}$ and $\dot{y}$ in the limit for very large $x$. Then $\dot{x}\approx x^2y$ and $\dot{y}=-x^2y$, so $\dot{y}/\dot{x}=-1$, or that the slopes of the direction filed is $-1$ for large $x$. Then, to compare $\dot{y}$ and $\dot{x}$ when $x$ is large, we have the expression $\dot{x}-(-\dot{y})=b-x$. Thus, if $x>b$ then $-\dot{y}>\dot{x}$.
