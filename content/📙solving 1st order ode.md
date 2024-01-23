---
title: 📙Solving 1st-Order ODEs
---

Below are a list of methods to approach [[📘order|📘1st-order]] [[📘ordinary]] differential equation of different forms. 

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

> [!example] Solving DEs with Integrating Factors
> 
> 1. Solve the [[📘initial value problem]] $\frac{dx}{dt} - x = \frac{11}{8} e^{-t/3}$ and $x(0)=-1$.
> > [!summary]- Solution
> >
> > We have $\rho(t)=e^{-t}$. Plugging in, we get the answer as 
> > $$
> > x(t)=\frac 1 {32} (e^t - 33 e^{-t/3}).
> > $$
>
> 2. See [[🗒️erie pollution|🗒️The Pollution of Lake Erie]].

### Method 2: Substitution

Substitution is the general method of assigning an intemediate variable $u$ to some function of $x$ and $t$, and replacing $\frac{dx}{dt}$ to $\frac{du}{dt}$. 

> [!example] Solving DEs with Substitution
>
> 1. Find the solution of the ODE 
> $$
> \frac{dx}{dt}=(x+t+3)^2.
> $$
> > [!summary]- Solution
> >
> > We let $u=x+t+3$ and $\frac{du}{dt}=\frac{dx}{dt}+1$. Then, we get 
> > $$
> > \int \frac{du}{u^2+1}=\int dt
> > $$
> > which is easily integratable. 
> 
> 2. Find the solution of the ODE
> $$
> 2tx \frac{dx}{dt}=4t^2+3x^2.
> $$ 
> > [!summary]- Solution
> > 
> > Dividing both sides by $2tx$, we get 
> > $$
> > \frac{dx}{dt}=2\frac t x + 1.5 \frac x t.
> > $$
> > We can substitute $u=x/t$, which allows us to integrate the expression.

### Method 3: Implicit form

If we have an implicit function 
$$
F(t, x(t))=C,
$$
we can take the partials to get 
$$
M(t,x)+N(t,x)\cdot \frac{dx}{dt}=0,
$$
where $M(t,x)=\frac{\partial F}{\partial t}$ and $N(t,x)=\frac{\partial F}{\partial x}$. In other words, 
$$
dF=Mdt+Ndx.
$$

Note that a solution exists if and only if
$$
\frac{\partial M}{\partial x}=\frac{\partial N}{\partial t}.
$$

> [!example] Solving DEs Implcitly
> 
> 1. Find the solution of the ODE 
> $$
> y^3dx+3y^2xdy=0.
> $$
> 
> > [!summary]- Solution
> > 
> > We need to find a function $F$ such that $F_t=x^3$ and $F_x=3x^2t$. Such a function is $x^3t$, so the implicit solution is given by $
> > $$
> > x^3t=C.
> > $$
> 
> 2. Find the solution of the ODE 
> $$
> (6tx-x^3)dt+(4x+3t^2-3tx^2)dx=0.
> $$
> > [!summary]- Solution 
> > 
> > To construct $F$, consider the integral 
> > $$
> > \int M(t, x) dt = \int(6tx-x^3)dt= 3xt^2-x^3t+g(x),
> > $$
> > where $g(x)$ is the integration constant as well as the antiderivative of $N(t, x)$. We can repeat the same process for $N$ to get $g(x)=2x^2+C$, so the final answer is 
> > $$ 
> > 3xt^2-x^3t+2x^2=C.
> > $$
