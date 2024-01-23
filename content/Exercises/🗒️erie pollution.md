---
title: 🗒️The Pollution of Erie
---

Lake Erie has a volume of $480$ cubic kilometers. The inflow from Lake Huron and outflow to Lake Ontario are both $350$ cubic kilometers per year. At $t=0$ the polution concentration of Erie is 5 times that of Huron. How long does it take for pollution in Erie to be twice that of Huron?

> [!summary] Solution
> 
> Let $c$ be the pollution concentration in Huron, and let $x(t)$ be the amount of pollutant in Erie at time $t$. Let $V=480$ be the volume of Lake Erie. The [[📘initial value problem|📘initial value]] is given by $x(0)=5cV$. The question asks us to find at what $t$ does $x(t)=2cV$. 
>
> The differential equation for this problem is given by
> $$
> \frac{dx}{dt}=rc-\frac{r}{V}x.
> $$
> We can use the method of [[📙solving 1st order ode#Method 1: Finding the Integrating Factor|📙finding the integrating factor]] to solve this differential equation. The resulting function is given by 
> $$
> x(t)=cV+4cVe^{-rc/V}.
> $$
> Solving for $x(t)=2cV$, we get $t=\frac{48}{35}\ln 4\approx 1.901$ years. 
