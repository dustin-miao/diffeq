---
title: 🗒️Water Bowl
---

Suppose you have a hemisphere-shaped bowl with a radius of $4$ feet. At $t=0$, the bowl is full of water. There is a circular hole at the bottom with a diameter of $1$ inch. Find the time when the tank empties. 

> [!summary]- Solution
> 
> Let $y(t)$ be the water level at time $t$, and let $V(t)$ be the volume of water at time $t$. By conservation of energy, we can dervie that the velocity of water per square inch is given by $v=\sqrt{2gy}$. Thus, we get our first equation, 
> $$
> \frac{dV(t)}{dt}=-av=-a\sqrt{2gy},
> $$
> where $a$ is the area of the hole. 
>
> Additionally, by the chain rule we know that 
> $$
> \frac{dV(t)}{dt}=\frac{dV(t)}{dy}\frac{dy}{dt}=A(y)\cdot \frac{dy}{dt},
> $$
> where $A(y)$ is the cross sectional area at height $y$ (note that this is because $V(y)=\int_0^y A(\bar{y})d\bar{y}$). The expression for $A(y)$ is given by 
> $$
> A(y)=\pi r^2=\pi(8y-y^2)
> $$
>
> Equating the two sides, we get the differential equation
> $$
> \pi(8y^2-y)\frac{dy}{dt}=-pi\left(\frac 1 {24}\right)^2 \sqrt{2(32)y}.
> $$
> Then, this becomes a simple [[📘initial value problem]]. Integating both sides and plugging the initial value of $y(0)=4$, we get that $t=2150$. 
