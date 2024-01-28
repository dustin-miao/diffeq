---
title: Population Models
---

Let $N$ be the number of members of a population. When the population size is unconstrained, the growth rate is proportional to the size of the population. Then, the equation for population growth is given by
$$
\dot{N}=rN
$$
for some positive constant $r$. The solutions of the differential equation is $N(t)=N_0e^{rt}$, where $N_0$ is the initial population. 

Suppose there is a constraint on the population $K$. Our improved model is given by 
$$
\dot{N}=rN(1-\frac N K).
$$
The [[📙phase portraits|📙phase portait]] of this equation is a parabola with roots at $N=0$ and $N=K$. Solving, we get 
$$
N(t)=\frac{K}{1+Ce^{-rt}}.
$$
This is known as a **logistic model**. For any positive starting population, $N$ will tend to $K$. For a starting population of $N=0$, the population will stay at $0$. 
