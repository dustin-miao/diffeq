---
title: 📙Solving 1st-Order ODEs
draft: true
---

Below are a list of ways to approach [[📘order|📘1st-order]] [[📘ordinary]] differential equation.

### Method 1: Finding the Integrating Factor

Suppose we are given a DE of the form 
$$
\frac{dx}{dt}+P(t)x=Q(t).
$$
Define $\rho(t)=e^{\int P(t)dt}$. We will multiply through by $\rho(t)$, which gives
$$
\frac{dx}{dt}\rho(t)+P(t)x\rho(t)=Q(t)\rho(t).
$$
Notice that the LHS is equal to $\frac{d}{dt}x(t)\rho(t)$. Substituting, this yields
$$
x(t)=\frac 1 {\rho(t)} \left[\int Q(t)\rho(t)dt + C\right].
$$

> [!example] Exercise
> 
> Solve the [[📘initial value problem]] $\frac{dx}{dt} - x = \frac{11}{8} e^{-t/3}$ and $x(0)=-1$.
> > [!summary] Solution
> >
> > We have $\rho(t)=e^{-t}$. Plugging in, we get the answer as 
> > $$
> > x(t)=\frac 1 {32} (e^t - 33 e^{-t/3}).
> > $$


