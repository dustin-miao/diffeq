---
title: Quantitive Approach to Stability
---

Suppose we are given the differential equation 
$$
\dot{x}=f(x)
$$
and an [[📘equilibrium points|📘equilibrum point]] $x^*$. By definition, $x^*$ must be an x-intercept in the [[📙phase portraits|📙phase portrait]]. Define the function $\eta(t)=x(t)-x^*$. Then, differentiating, we get
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
