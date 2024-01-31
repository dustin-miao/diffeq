---
id: 📙bifuracations
aliases: []
tags:
  - "24-01-31"
title: 📙Bifurcations
---
 
Suppose we have the differential equation $\dot{x}=r+x^2$ for some parameter $r$. Let's consider the three [[📕phase portraits]] that result from $r<0$, $r=0$, and $r>0$:
1. For $r<0$, we have two critical points, where one is an [[📘attractor]] and the other is a [[📘repeller]]
2. For $r=0$, we have one semi-stable critical point at $x=0$
3. For $r>0$, we have no critical points 

This is a specific type of **bifurcation** known as **saddlenode bifurcation**. 

> [!example] Another Saddlenode Example 
> 
> 1\. Given the differentian equation $\dot{x}=f(x)=r-x^2$. Use [[📙linear stability analysis]] to determine the quality of the [[📘equilibrium points]] and determine the form of the [[📕flow diagram]]
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
> Find the intersection point $r$ and plot the [[📕flow diagram]].
> 
> > [!summary]- Solution 
> > 
> > We can graph $y=r+\frac x 2$ and $y=\frac x {x+1}$ to find the [[📘equilibrium points]]. Differentiating both equations with respect to $x$, we get $r=\frac 3 2 \pm \sqrt{2}$ and $x=-1\pm \sqrt{2}$. 
> >
> > The [[📕flow diagram]] is given xy $r=\frac x {x+1} - \frac 1 2 x$. 
