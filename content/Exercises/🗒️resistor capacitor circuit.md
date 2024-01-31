---
id: 🗒️resistor capacitor circuit
aliases: []
tags: []
title: 🗒️Resistor Capacitor Circuit
---

Suppose you have a battery of voltage $V_0$ that is wired in series to a resistor with resistance $R$ and a capacitor with capacitance $C$. Find the differential equation that models this system and the [[📘equilibrium points]] of the equation.

> [!summary]- Solution
>
> From physics, we know that $V=IR$ and $V=Q/C$, where $I$ is the current and $Q$ is the charge. By Kirchoff's law, we have 
> $$
> V_0+IR+\frac Q C =0.
> $$
> Note that $I=\dot{Q}$, so we can express this equation as 
> $$
> \dot{Q}=\frac{V_0}{R}-\frac{Q}{CR}.
> $$
> The [[📘equilibrium points|📘equilibrium point]] at $Q=CV_0$ is an [[📘attractors|📘attractor]], and the [[📕phase portrait]]ne.
