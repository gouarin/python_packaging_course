Cubic Spline
============

We consider here a cubic spline passing through the points :math:`(x_i,y_i)` with :math:`a=x_1<\ldots<x_n=b`, that is, a class function :math:`{\mathcal C}^2` on :math:`[a, b]` and each restriction at the interval :math:`[x_{i-1},x_i]`, :math:`1\leq i\leq n`, is a polynomial of degree less than 3. We will note :math:`S` such a spline. His equation is given by

.. math::
    S_i(x) =  Ay_i + By_{i+1} + Cy''_i+ D y''_{i+1}, \qquad x_{i}\leq x\leq x_{i+1},

where

.. math::
    A = \frac{x_{i+1}-x}{x_{i+1} - x_i} \qquad \text{et} \qquad B = \frac{x-x_i}{x_{i+1} - x_i},

.. math::
    C = \frac{1}{6}\left(A^3-A\right)\left(x_{i+1}-x_i\right)^2 \qquad \text{et} \qquad D = \frac{1}{6}\left(B^3-B\right)\left(x_{i+1}-x_i\right)^2.

If we derive this equation twice with respect to :math:`x`, we get

.. math::
    \frac{d^2S(x)}{d x} = Ay''_i + By''_{i+1}.

Since :math:`A = 1` in :math:`x_i` and :math:`A = 0` in :math:`x_ {i + 1}` and conversely for :math:`B`, we can see that the second derivative is continuous at the interface of the two intervals :math:`[x_{i-1}, x_{i}]` and :math:`[x_{i}, x_{i + 1}]`.

It remains to determine the expression of :math:`y''_i`. To do this, we will calculate the first derivative and impose that it is continuous at the interface of two intervals. The first derivative is given by

.. math::
    \frac{dy}{dx}=\frac{y_{i+1}-y_{i}}{x_{i+1}-x_{i}}-\frac{3A^2-1}{6}(x_{i+1}-x_{i})y''_i+\frac{3B^2-1}{6}(x_{i+1}-x_{i})y''_{i+1}.

We therefore want the value of the first derivative in :math:`x = x_i` over the interval :math:`[x_{i-1}, x_{i}]` to be equal to the value of the first derivative in :math:`x = x_i` over the interval :math:`[x_{i}, x_{i + 1}]`; which gives us for :math:`i = 2, \dots, n-1`

.. math::
    a_iy''_{i-1}+b_iy''_i+c_iy''_{i+1}=d_i,

with

.. math::
    \begin{array}{l}
    a_i = \frac{x_i-x_{i-1}}{x_{i+1}-x_{i-1}}\\
    b_i = 2\\
    c_i = \frac{x_{i+1}-x_{i}}{x_{i+1}-x_{i-1}}\\
    d_i = \frac{6}{x_{i+1}-x_{i-1}}\left(\frac{y_{i+1}-y_{i}}{x_{i+1}-x_{i}}-\frac{y_{i}-y_{i-1}}{x_{i}-x_{i-1}}\right).
    \end{array}

So we have :math:`n-2` linear equations to calculate the :math:`n` unknowns :math:`y''_i` for :math:`i = 1, \dots, n`. So we have to make a choice for the first and last values ​​and we will take them equal to zero. We can recognize the resolution of a system with a tridiagonal matrix. It is then easy to solve it by using the algorithm of Thomas which one recalls the principle

.. math::
    c'_i=\left\{ 
    \begin{array}{lr}
    \frac{ci}{b_i}&i=1\\
    \frac{c_i}{b_i-a_ic'_{i-1}}&i=2,\dots,n.
    \end{array}
    \right.

.. math::
    d'_i=\left\{ 
    \begin{array}{lr}
    \frac{di}{b_i}&i=1\\
    \frac{d_i-a_id'_{i-1}}{b_i-a_ic'_{i-1}}&i=2,\dots,n.
    \end{array}
    \right.

The solution is then obtained by the formula

.. math::
    \begin{array}{l}
    y''_n = d'_n \\
    y''_i = d'_i-c'_iy''_{i+1} \qquad \text{pour} \qquad i=n-1,\dots,1.
    \end{array}

