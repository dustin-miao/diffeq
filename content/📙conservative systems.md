---
id: 📙conservative systems
aliases: []
tags:
  - "24-03-11"
  - "24-03-13"
title: 📙Conservative Systemts
---

A conservative system is one that can be modeled as $m\ddot{x}=F(x)$. In particular, we can define $F(x)=-\frac{dV}{dx}$, which yields 
$$
m\ddot{x}+\frac{dV}{dx}= 0.
$$
Multiplying by $\dot{x}$, we get 
$$
m\ddot{x}\dot{x}+\frac{dV}{dx}\dot{x}=0. 
$$
This allows us to factor out a $\frac{d}{dt}$ term: 
$$
\frac{d}{dt}\left[\frac 1 2 m\dot{x}^2+V(x)\right]=0. 
$$
This gives us the conservation of energy equation, where $\frac 1 2 m\dot{x}^2+V(x)$ is a constant $E$. Energy, in this case, is a conserved quantity. 

Formally, a **conserved quantity** is a real valued continuous function $E(x)$ that is constant on trajectories. In other words,
$$
\frac{dE}{dt}= 0.
$$
We require that $E(x)$ be nonconstant on different trajectories to avoid trivial cases. Thus, all conservative systems cannot have any [[📘attractors|attracting fixed points]].

> [!example] Example of a Conservative System 
> 
> Suppose we have a conservative system given by 
> $$
> V(x) = -\frac 1 2 x^2 + \frac 1 4 x^4.
> $$
> Find the phase portrait. Assume that $x=1$.
>
> > [!summary]- Solution
> > 
> > Denote $y=\dot{x}$, so $\dot{y}=V'(x)=x-x^3$. Solving this system, we get the equilibrium points $(0,0)$, $(1,0)$, $(-1,0)$. We find the Jacobian as 
> > $$
> > A = \begin{bmatrix} 0 & 1 \\ 1-3x^2 & 0 \end{bmatrix}.
> > $$
> > Substituting and solving for $\Delta$ and $\tau$ for each equilibrum point, we get that $(0,0)$ is a saddle and $(1,0)$ and $(-1,0)$ are centers. In this case, the centers are truly centers because the system is conservative (so the energy is constant). 
> > 
> > ![[img/conservative-alien-example.png]]
> > 
> > These are known as **homoclinic orbits**, or orbits that start and end at the same fixed point. 

### Reversible systems

A system is **reversible** if the dynamics look the same whether time runs forward or backward. In other words, the system is invariant under $t\to -t$ and $y\to -y$. If we have the system $\dot{x}=f(x,y)$ and $\dot{y}=g(x,y)$, then the system is reversible only if $f(x,y)$ is odd in $y$ and $g$ is even in $y$. 

> [!example] Example of a Reversible System
>
> Find the fixed point and attempte to find the phase portrait of the system given by $\dot{x}=-2\cos x - \cos y$ and $\dot{y} = -2\cos y - \cos x$. Is this system conservative? Is it reversible?

### Pendulums

A pendulum with angle $\theta$ and length $L$ satisfies the differential equation
$$
\frac{d^2\theta}{dt^2} + \frac g L \sin \theta = 0.
$$

We define two auxiliary variables $\omega=\sqrt{g/L}$ and $\tau=\omega t$, and then redefine $\dot{\theta}=\frac{d\theta}{d\tau}$. Our system now becomes 
$$
\ddot{\theta}=\sin \theta=0
$$
where $\ddot{\theta}$ is with respect to $\tau$. Let $v=\dot{\theta}$. The new system is given by $\dot{\theta}=v$ and $\dot{v}=-\sin \theta$. Then, the fixed ponits are at $(\theta^*, v^*)=(k\pi, 0)$. We will only consider the points between $0$ and $2\pi$, so we consider only $(0,0)$ and $(\pi, 0)$. 

The point at $(0,0)$ is a linear center. Furthermore, because the system is linear and conservative (most mechanical systems are conservative because of conservation of energy). To find the conserved quantity, consider 
$$
\dot{\theta}(\ddot{\theta}+\sin\theta)=0.
$$
Integrating, we get that 
$$
C=\frac 1 2 \dot{\theta}^2 - \cos \theta.
$$


