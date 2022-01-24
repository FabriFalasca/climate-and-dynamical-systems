# climate-and-dynamical-systems

Contacts: Fabrizio Falasca (fabrifalasca@gmail.com)

****** This readme and repository are under construction ****** 

## Summary

The climate system is multiscale, high-dimensional and nonlinear. However, spatiotemporal recurrences of the system hint to the presence of low-dimensional manifolds containing the high-dimensional climate trajectory. These objects are commonly referred to as "intertial manifolds" or "attractors". Lots of pointers on this can be found in this thesis https://chaosbook.org/projects/gudorfThesis.pdf and in ChaosBook https://chaosbook.org/.

Characterizing geometrical and topological properties of the climate attractor is an useful step for comprehensively characterize, investigate and study spatiotemporal climate fields. Furthermore, correctly resolving the attractor represents a useful step for evaluation of climate model outputs. Here we collect some data mining algorithms and methods that we found useful in our own research.

# Folder local_dimension_and_persistence

Metrics to compute local (instanteneous) properties of the attractor: local dimension and stability (or persistence). These metrics have been developed at the interface of Extreme Value Theory (EVT) and dynamical systems. Reference book: see https://arxiv.org/pdf/1605.07006.pdf 
Among the many weather/climate applications see this: https://www.nature.com/articles/srep41278 

Here you find an application of these metrics for (a) the Lorenz System and (b) weekly temperature anomalies in the Pacific (notice that these metrics allow to study the system by looking at more than one variable at a time as shown in https://arxiv.org/pdf/2110.03614.pdf ).

NOTE: the metrics shown here have been downloaded from Yoann Robin github https://github.com/yrobink/CDSK (Thanks Yoann).

# Folder Manifold_learning

TO ADD

Collection of some manifold learning algorithm we found useful to investigate high-dimensional climate dynamics through low-dimensional, nonlinear projections.

In this repository we will add new codes, explorations and tests hopefully useful to the climate community for data mining of complex, high-dimensional climate fields from a dynamical system point of view.

# Reference

- ChaosBook https://chaosbook.org/
- Extremes and recurrences in dynamical systems https://arxiv.org/pdf/1605.07006.pdf 
- Falasca, F. and Bracco, A. Exploring the Climate system through manifold learning (2021) https://arxiv.org/abs/2110.03614
