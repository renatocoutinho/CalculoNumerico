#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Este trabalho está licenciado sob a Licença Creative Commons Atribuição-CompartilhaIgual 3.0 Não Adaptada. Para ver uma cópia desta licença, visite http://creativecommons.org/licenses/by-sa/3.0/ ou envie uma carta para Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Author: Pedro H A Konzen - 08/2016
'''

import numpy as np
import scipy as sci
from scipy import optimize
import matplotlib.pyplot as plt

#font settings
plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=12)

#canvas
fig = plt.figure(figsize=(2.5,2.5), dpi=300)

#axes definitions
ax = plt.subplot(1,1,1)

ax.set_xlim(1.6,1.8)
ax.set_ylim(1.4,2)

def fun(x):
    return x - 0.5*(x*np.exp(x)-10)

a = 1.6
b = 1.8
x = np.linspace (a, b)

ax.plot(x, fun(x))
ax.annotate("$y=g_1(x)$",xytext=(1.63,1.875), xy=(1.71,1.975),arrowprops=dict(arrowstyle="->",lw=0.2))

x = np.linspace(a,b)
ax.plot(x, x, 'k--')
ax.annotate("$y=x$",xytext=(1.625,1.525), xy=(1.625,1.625),arrowprops=dict(arrowstyle="->",lw=0.2))


#ponto fixo
def g(x): return fun(x)-x
xstar = sci.optimize.fsolve(g,1.7)
print(xstar)
ax.plot([xstar],[xstar],'ro',markersize=4)
ax.text(xstar+0.01,xstar-0.025,"$x^{\!*}$")

#iteração
x = 1.74
ax.text(x+0.005,fun(x)+0.02,"$x^{(1)}$")
ax.plot([x],[fun(x)],'ko',markersize=3)
ax.arrow(x, 1.4, 0, fun(x)-1.4, head_width=0.0075, head_length=0.025, length_includes_head=True, color='red', lw=0.1)
ax.arrow(x, fun(x), fun(x)-x, 0, head_width=0.02, head_length=0.0075, length_includes_head=True, color='red', lw=0.5)
x = fun(x)
ax.text(x-0.03,fun(x)-0.01,"$x^{(2)}$")
ax.plot([x],[fun(x)],'ko',markersize=3)
ax.arrow(x, x, 0, fun(x)-x, head_width=0.0075, head_length=0.025, length_includes_head=True, color='red', lw=0.1)

fig_file =  "ponto_fixo_instavel"
fig.savefig(fig_file+".eps", bbox_inches='tight')
fig.savefig(fig_file+".pdf", bbox_inches='tight')
fig.savefig(fig_file+".png", bbox_inches='tight')
fig.savefig(fig_file+".svg", bbox_inches='tight')
