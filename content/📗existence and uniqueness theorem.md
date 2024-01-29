---
id: 📗existence and uniqueness theorem
aliases: []
tags:
  - "24-01-25"
title: 📗Existence and Uniqueness Theorem
---

Consider $\dot{x}=f(x)$ and $x(0)=x_0$. Suppose $f(x)$ and $f'(x)$ are continuous on an open interval on the $x$-axis and $x_0$ is a real number. Then, the [[📘initial value problem|📘initial value problem]] has a unique solution $x(t)$ for some time interval $(-T, T)$ about $t=0$. 

> [!example] Pathological Cases
>
> 1. Find the solutions to the differential equation
> $$
> \dot{x}=x^{1/3}
> $$
> at $x(0)=0$. 
> 
> > [!summary]- Solution
> >
> > Cross-multiplying and integrating, we get $x(t)=\left(\frac 2 3 t)^{3/2}$. However, we also have the trivial solution $x(t)=0$. However, by looking at the [[📙phase portraits|📙phase portrait]], we see the derivative at $0$ is undefined, so this does not satisfy the conditions specified by the theorem. 
> 
> 2. Find the solutions to the differential equation 
> $$
> \dot{x}=1+x^2
> $$
> at $x(0)=0$. 
> 
> > [!summary]- Solution 
> > 
> > We get the solution $x=\tan t$. Notice that the solution exists in the internval $-\pi/2<t<\pi/2$, and blows up in finite time.  
