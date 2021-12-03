# climate-and-dynamical-systems

Contacts: Fabrizio Falasca (fabrifalasca@gmail.com)

The climate system is multiscale, high-dimensional and nonlinear. However, spatiotemporal recurrences of the system hint to the presence of low-dimensional manifolds containing the high-dimensional climate trajectory. These lower (than a full state space) objects are commonly referred to as attractors or inertial manfifolds (more in the Introduction section of this amazing thesis https://chaosbook.org/projects/gudorfThesis.pdf and even more in https://chaosbook.org/).
Climate is a nonlinear, dissipative system and, when trends are removed, we expect its trajectory to live on an attractor. Characterizing geometrical and topological properties of the climate attractor is an useful step for comprehensively characterize, investigate and study spatiotemporal climate fields. Furthermore, correctly resolving the attractor represents a useful step for evaluation of climate model outputs. Here we collect some data mining algorithms and methods that we found useful in our own research.

****** This readme and repository are under construction.****** 

For now you will find the two metrics proposed by Valerio Lucarini, Davide Faranda &  friends in this book https://arxiv.org/pdf/1605.07006.pdf . The two metrics proposed quantify instaneous properties of high dimensional trajectories via the local dimension and stability. Lots of points to the literature can be found here: https://arxiv.org/pdf/2110.03614.pdf . The metrics, downloaded from Yoann Robin page (https://github.com/yrobink/CDSK/tree/master/python/CDSK . Thanks Yoann!) are showcased for the Lorenz system.
For a more insightful analysis of the Lorenz system using the local dimension and stability metrics, please give a look at the supplemental material of Davide's paper here: https://www.nature.com/articles/srep41278 
They run the system for way more time steps than we do and are able to recover the classical estimates of the average attractor dimension. In this notebook, we run it for way less time steps: the main point here is mainly to showcase these indicators. 

A paper adopting such metrics for atmospheric fields can be found here : https://www.nature.com/articles/srep41278 . A new paper applying the local dimension metric to ocean flows has been recently accepted in GRL and will be posted soon. 

In this repository we will also add some algorithms for manifold learning that have been shown to be useful in climate applications, see https://arxiv.org/pdf/2110.03614.pdf 

In this repository we will add new codes, explorations and tests hopefully useful to the climate community for data mining of complex, high-dimensional climate fields from a dynamical system point of view.
