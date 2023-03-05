1  # !/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : startingmotif_functions.py
4  # @Author: Gemma van der Voort
5  # @Date  : 23-02-23
6  # @Desc  : script for calculating ODE systems, including a simple visualisation
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp
from startingmotif_functions import motif_odes

# parameters:
param_df = pd.read_csv('data/startingmotif_parameter_values.csv')
params = list(param_df.loc[:, 'value'])
par_names = list(param_df.loc[:, 'parameter name'])
# variables:
variable_df = pd.read_csv('data/startingmotif_variable_initial_values.csv')
y0 = list(variable_df.loc[:, 'initial value'])
var_names = list(variable_df.loc[:, 'Variable name'])

# time steps
t0, tf = 0, 7  # start and final time point
# t = np.linspace(t0, tf, num=1000) # optional: fix amount of steps. Needed for some solvers

# solving
sol = solve_ivp(motif_odes, (t0, tf), y0, args=(params,))

# simple visualisation
f, axes = plt.subplots(1, 2, figsize=(25, 20))
for i, ax in zip(range(len(var_names)), axes.flat):
    ax.set_title(var_names[i], fontsize=30)
    ax.set_xlabel('Time(days)')
    ax.set_ylabel('Cells (ng/ml)')
    # ax.set_yscale('log') # sometimes useful
    ax.plot(sol.t, sol.y[i])
f.show()
