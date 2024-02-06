---
id: 📙bifurcations
aliases:
  - Sattlenode Bifurcations
tags:
  - "24-01-31"
  - "24-02-02"
  - "24-02-06"
title: 📙Bifurcations
---

### Sattlenode Bifurcations

Suppose we have the differential equation $\dot{x}=r+x^2$ for some parameter $r$. Let's consider the three [[📕phase portraits]] that result from $r<0$, $r=0$, and $r>0$:
1. For $r<0$, we have two critical points, where one is an [[📘attractor]] and the other is a [[📘repeller]]
2. For $r=0$, we have one semi-stable critical point at $x=0$
3. For $r>0$, we have no critical points 

This is a specific type of **bifurcation** known as **saddlenode bifurcation**. In the general case, the **form factor** is given by $\dot{x}=r\pm x^2$. 

> [!example] Saddlenode Examples
> 
> 1\. Given the differentian equation $\dot{x}=f(x)=r-x^2$. Use [[📙linear stability analysis]] to determine the quality of the [[📘equilibrium points]] and determine the form of the [[📕flow diagrams|📕flow diagram]]
>
> > [!summary]- Solution
> > 
> > For $r>0$, we have $x^*=\pm\sqrt{r}$, so the root at $\sqrt{r}$ is stable and the root at $-\sqrt{r}$ is unstable. For $r=0$, the equilibrum point is semi-stable.
> 
> See [[🗒️saddlenode bifurcation]].

We can show that all saddlenode bifurcations take the form $\dot{x}=r\pm x^2$. Take, for instance, the example posed in [[🗒️saddlenode bifurcation]]. By expading the taylor serios of $e^{-x}$, we get
$$
\begin{align*}
\dot{x}&=r-x-e^{-x} \\
&=r-x-\left[1-x+\frac{x^2}{2!}-\frac{x^3}{3!}+\dots\right] \\
&=(r-1)-\frac 1 2 x^2+\mathcal{O}(x^3).
\end{align*}
$$
Specifically, we need $2$ local fixed points to collide and disappear, meaning that $f(x)$ must be locally parabolic.

In the general case, let $\dot{x}=f(x,r)$. At the bifurcation point $x=x^*$, let $r=r_c$. Consider the Taylor series expansion of $f(x,r)$:
$$
\dot{x}=f(x^*,r_c)+(x-x^*)\frac{\partial f}{\partial x}\vert_{(x^*,r_c)}+(r-r^*)\frac{\partial f}{\partial r}\vert_{(x^*,r_c)}+\frac 1 2 (x-x^*)^2\frac{\partial^2 f}{\partial x^2}\vert_{(x^*,r_c)} +\dots.
$$
Like before, we will ignore the cubic terms in $(x-x^*)$ and quadratic terms in $(r-r_c)$. We get 
$$
\dot{x}=a(r-r^*)+b(x-x^*)^2,
$$
which takes the form of the original equation. 

> [!example] More Saddlenode Example 
> 
> You are given the following differential equation:
> $$
> \dot{x}=r+\frac 1 2 x - \frac x {1+x}.
> $$
> Find the intersection point $r$ and plot the [[📕flow diagrams|📕flow diagram]].
> 
> > [!summary]- Solution 
> > 
> > We can graph $y=r+\frac x 2$ and $y=\frac x {x+1}$ to find the [[📘equilibrium points]]. Differentiating both equations with respect to $x$, we get $r=\frac 3 2 \pm \sqrt{2}$ and $x=-1\pm \sqrt{2}$. 
> >
> > The [[📕flow diagrams|📕flow diagram]] is given xy $r=\frac x {x+1} - \frac 1 2 x$. 

### Transcritical Bifurcations 

The **form factor** of **transcritical bifurcations** is given by $\dot{x}=rx-x^2$, where $r$ is the parameter. The three [[📕phase portraits]] for $r<0$, $r=0$, and $r>0$ take the following form:
- For $r<0$, the phase portrait is a parabola with an [[📘repeller]] at $r$ and an [[📘attractor]] at $0$.
- For $r=0$, the phase portrait is a downward-opening parabola with a semi-stable [[📘equilibrium points|📘fixed point]] at $0$.
- For $r>0$, the phase portrait is a parabola with an [[📘attractor]] at $r$ and a [[📘repeller]] at $0$.

The [[📕flow diagrams|📕flow diagram]] the differential equation above consists of two lines with equations $x=0$ and $x=r$. The former is unstable (dashed) for positive $r$, and the latter is unstable for negative $r$. 

In general, the definition of a transcritical bifurcation is a [[📘equilibrium points|📘fixed point]] that exists for all values of the parameter. However, the [[📙stability]] of the point may change with $r$.

> [!example] Transcritical Examples
> 
> For each of the following differential equation, find the form of the [[📕flow diagrams|📕flow diagram]]:
> 1. $\dot{x}=r\ln x + x - 1$
> 2. $\dot{x}=x-rx(1-x)$ 
> 
> > [!summary]- Solution 
> > 
> > 1\. By inspection, we determine that $x=1$ is a fibed point. Otherwise, we can use [[📙solving 1st order ode#Method 2: Substitution|📙u-substitution]] by setting $u=x-1$, $\dot{u}=\dot{x}$. This gives 
> > $$
> > \dot{u}=r\ln(u+1)+u =r\left(u-\frac {u^2}{2} +\mathcal{O}(u^3)\right)+u 
> > $$
> > which is the general form of the equation. Thus, the bifurcation point happens at $r=-1$. 
> >
> > 2\. Graphing the [[📕phase portraits|📕phase portrait]]or several values of $r$, we get the following diagram:
> > ![[img/transcritical-example-diagram.png]]
> > 
> > For the [[📕flow diagrams|📕flow diagram]], we get the equations $x=rx(1-x)$. There is a horizontal line at $x=0$ and a hyperbola at $x=\frac{r-1}{r}$, with an intersection point at $r=1$. 

This type of bifurcations is useful for modeling **lasers**. From the textbook
> [!quote] 
> 
> Each atom can be thought of as a little antenna radiating energy. When the pumping is relatively weak, the laser acts just like an ordinary lamp; the excited atoms oscillate independently of one another and emit randomly phased light waves. 
 
Let us consider a simplified model of the essential physics. The dynamical variable is the number of photons $n(t)$ in the laser field. Its rate of change is given by 
$$
\dot{n} = \text{gain} - \text{loss} = GnN-kn.
$$
where $G$ is the gain coefficient and $k$ is a rate constant; the repricol $r=1/k$ represents the typical lifetime of a photon in the laser. 

Then, suppose that in the absence of laser action, the pump keeps the number of excited atoms fixed at $N_0$. Then the actual number of excited atoms will be reduced by the laser process. Spcificially, we assume 
$$
N(t)=N_0-\alpha n 
$$ 
where $alpha>0$ is the rate at which atoms drop back to their ground states. Solving, we get 
$$
\begin{align*}
\dot{n}(t)&=Gn(N_0-\alpha n)-kn \\
&= (GN_0 - k)n - \alpha Gn^2.
\end{align*}
$$

In this case, $N_0$ is the parameter. There are three cases: $N_0<\frac k G$, $N_0=\frac k G$, and $N_0>\frac k G$. In this case, we only care about positive $n$. 
- In the first case, the [[📘equilibrium points|📘fixed point]] at $n=0$ is [[📘attractors|📘stable]]. 
- In the second case, the [[📘equilibrium points|📘fixed point]] at $n=0$ is semi-stable.
- In the third case, [[📘equilibrium points|📘fixed point]] at $n=0$ is [[📘repellers|📘unstable]]

### Pitchfork Bifurcation 

The **form factor** of a **pichfork bifurcation** is given by $\dot{x}=rx-x^3$. 
- For $r\leq 0$, the only fixed point is at $0$. 
- For $r>0$, there two more fixed points at $\pm\sqrt{r}$ along with the original at $0$.

![[img/pitchfork-bifurcation-example.png]]

The [[📕flow diagrams|📕flow diagram]] resembels a pitchfork, with a solid line at negative $r$ for $x=0$, a dashed line at positive $x$ for $x=0$ alongside two additional cubic lines branching off the center line. Holistically, a pitchfork bifurcation is defined as one where the points appear in pairs. 

> [!example] Pitchfork Bifurcation examples 
> 
> 1\. Find the [[📕flow diagrams|📕flow diagram]] of the differential equation $\dot{x}=rx+4x^3$.
> 
> > [!summary]- Solution 
> > 
> > ![[img/pitchfork-bifurcation-example-diagram-1.png]]
> > 
> > Only the $x=0$ for $r<0$ is [[📘repellers|📘unstable]]. 
> 
> 2\. Find the [[📕flow diagrams|📕flow diagram]] of the differential equation $\dot{x}=x+\frac{rx}{1+x^2}$. 
> 
> > [!summary]- Solution 
> > 
> > We can reduce the equation to $\dot{x}=\frac{(r+1)x+x^3}/{1+x^3}$, so we know that the transition point happens at $r=-1$. 
> > 
> > ![[img/pitchfork-bifurcation-example-diagram-2.png]]
> >


In a **subcritical** pitchfork bifurcation, a single stable [[📘equilibrium points|📘equilibrium point]] changes from [[📘attractors|📘stable]] to [[📘repellers|📘unstable]] and branches into two new [[📘attractors|📘stable]] points. In a **subcritical** case, it changes from a [[📘attractors|📘stable]] to an [[📘repellers|📘unstable]] [[📘equilibrium points|📘equilibrium point]], as shown in the example above. 

Consider the [[📙potentials|📙potential plot]] of $\dot{x}=rx-x^3$ for $r<0$, $r=0$, and $r>0$. Recall that $\dot{x}=f(x)=-\frac{dV}{dx}$. We get that $V(x)=-\frac r 2 x^2+\frac{x^4}{4}$. Graphing, this corroborates our knowledge about the quality of the [[📘equilibrium points]].

Lastly, consider the [[📕flow diagrams|📕flow diagram]] of $\dot{x}=rx+x^3-x^5$:

![[img/transcritical-fifth-degree-diagram.png|400x400]]

Let $r_s$ be the minimum possible value of $r$ that the fifth-degree function achieves. In the case where $r_s<r<0$, the origin is stable for small perterbations. If on the other hand we have an initial state at $x\approx 0$, it will jump to the next stable portion along the curve. 
