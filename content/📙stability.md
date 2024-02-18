---
id: 📙stability
aliases:
  - 📙linear stability analysis
tags:
  - "24-01-25"
title: 📙Quantitive Approach to Stability
---

Suppose we are given the differential equation 
$$
\dot{x}=f(x)
$$
and an [[📘equilibrium points|equilibrium point]] $x^*$. By definition, $x^*$ must be an x-intercept in the [[📕phase portrait|phase portrait]] fine the function $\eta(t)=x(t)-x^*$. Then, differentiating, we get
$$
\dot{\eta(t)}=\frac{d}{dt}(x(t)-x^*)=\dot{x}=f(x).
$$
Since $x(t)=\eta(t)+x^*$, the expression is equivalent to $f(\eta(t)+x^*)$. We can approximate this with a linear expression by taking the first two terms of the Taylor series:
$$
f(x^*+\eta(t))=f(x^*)+\eta(t)f'(x^*)+\mathcal{O}(\eta(t)^2).
$$
By definition, $f(x^*)=0$, so the final expression becomes
$$
\dot{\eta}=\eta f'(x^*).
$$
This implies that the perterbation grows exponentially when $f'(x^*)>0$, and decays exponentially when $f'(x^*)<0$. 

The quantitity $\lvert f'(x^*)\rvert$ is the amount of time required for $x(t)$ to vary significantly around the critical point. This is called a **time scale** because it tells us the amount of time for the dynamical system to appear very different from the critical point.


> [!example] Another Perspective of Prior Problems
> 
> Find and categorize the [[📘equilibrium points|equilibrium points]] of the following differential equations:
> 1. $\dot{x}=\sin x$
> 2. $N(t)=rN(1-N/k)$ (see [[📙population models|population models]])
> 
> > [!summary]- Solution
> > 
> > 1\. The critical points are given by $x^*=k\pi$ for $k\in\mathbb{Z}$. Then, 
> > $$
> > f'(x^*)=\cos x \vert_{x^*}=\begin{cases} 1 & k\text{ even} \\ -1 & k\text{ odd}\end{cases}.
> > $$
> > For even $k$, the point is stable, and for odd $k$ the point is unstable
> > 
> > 2\. We have $N^*=0,K$, so $f'(N^*)=r-\frac{2r}{K}N$ is $r$ at $N^*=0$ (making it unstable) and $-r$ at $N^*=K$ (making it stable).


Note that if $f'(x^*)=0$, then we can't draw any conclusions about the function. In this case, we can use [[📙phase portraits|phase portraits]] instead. 

> [!example] Examples of DEs with a Derivative of 0
>
> Categorize the [[📘equilbrium points|equilbrium points]] of the following functions:
> 1. $\dot{x}=-x^3$
> 2. $\dot{x}=x^3$
> 3. $\dot{x}=x^2$
> 4. $\dot{x}=0$
>
> > [!summary]- Solution
> > 1. Stable 
> > 2. Unstable 
> > 3. Semi-Stable
> > 4. Neither


For more examples, see [[🗒️linear stability analysis]].
