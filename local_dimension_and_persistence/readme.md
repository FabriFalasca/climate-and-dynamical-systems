*** Under construction ***

Two example where we run the local dimension and persistence metrics proposed by Valerio Lucarini, Davide Faranda & friends in this book https://arxiv.org/pdf/1605.07006.pdf . Original code for computation of the metrics has been downloaded from Yoann Robin repository https://github.com/yrobink/CDSK/tree/master/python/CDSK . Thanks Yoann!

- Local dimension metric: it quantifies the density of each point in state space. It is therefore linked to "local degree of freedoms" of each state space point.

- Local stability/persisteence: it is bounded from 0 to 1. Very low values of the stability metrics implies that the trajectory persists more in the neighborhood of a state point (and opposite in case of high values of stability).

First example: Lorenz_system. 
Here we simply run the metrics to quantify each state of the Lorenz system in chaotic regime. We do not integrate the system so long in time...the notebook is just there in order to showcase such metrics with a familiar example. We also add a simple Mathematica Notebook to run the local dimension metric.

Second example: temperature in the tropical Pacific sector in the last 40 years. We use daily data from ERA5 reanalysis.
