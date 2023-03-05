1  # !/usr/bin/env python
2  # -*- coding: utf-8 -*-
3  # @File  : startingmotif_functions.py
4  # @Author: Gemma van der Voort
5  # @Date  : 23-02-23
6  # @Desc  : from Hart et al. (2012), Fig. 4.


def motif_odes(t, variables, params):
    """
    network motif from Hart et al. (2012), Fig. 4. compatible with scipy.integrate.solve_ivp.
    :param t: time point at which the ODE system has to be evaluated.
    :param variables: list of ints for the values of the variables
    :param params: list of ints for the values of the parameters
    :return: updated variable values
    """
    X1, C = variables
    beta_0, alpha, beta_3, alpha_1, X0 = params
    f_c = C / (C + 3)
    dX1 = beta_0 * f_c * X0 - alpha * X1
    dC = beta_3 - alpha_1 * f_c * X0
    return dX1, dC
