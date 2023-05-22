import numpy as np
import scipy.io
from scipy import signal

# PCA analysis
from sklearn.decomposition import PCA
# Isomap
from sklearn.manifold import Isomap

# Distances
from scipy import stats
from scipy.spatial.distance import cdist

# Main input
# np.shape(data) = (n_observations, n_features) (so, [Time,state space dimension])

def pca_manifold_learning(data,n_components):

    # T = length of each time series
    Time = np.shape(data)[0]
    # N = dimensionality of the (temperature) state space
    N = np.shape(data)[1]

    # we set svd_solver = 'full' ---> it computes the SVD of the Gram matrix
    pca = PCA(n_components=n_components, svd_solver = 'auto')
    pca.fit(data)

    # These are going to be the PCs
    projected_embedding = pca.fit_transform(data)

    # These are going to be the variance explained by each component
    variance_explained = pca.explained_variance_ratio_

    # pcs are the projected embedding normalized
    pcs = projected_embedding/np.std(projected_embedding,axis=0)

    # Spatial components can be computed as a regression over the data
    components = (1/(Time-1))*np.dot(pcs.T,data)

    # Let's compute also the Residual Variance

    # Step (a)
    # Compute the Euclidean Matrix
    D_Euclidean = cdist(data,data,'euclidean')

    # (b.1) Compute the distance matrix in the LOW dimensional embedding using Euclidean distance
    # (b.2) Compute the correlation r between the distance matrix D_G and D_Y
    # (b.3) Compute the residual variance (1 - r^2)

    # Initialize the correlation vector
    r = []

    # We work with symmetric matrices: let's consider only the upper triangular part
    flatten_D_Euclidean = D_Euclidean[np.triu_indices(D_Euclidean.shape[0],k=1)]

    for i in np.arange(1,n_components+1):

        D_Y = cdist(projected_embedding[:,0:i], projected_embedding[:,0:i], 'euclidean')
        flatten_D_Y = D_Y[np.triu_indices(D_Y.shape[0],k=1)]
        r.append(stats.pearsonr(flatten_D_Y,flatten_D_Euclidean)[0])

    r = np.array(r)

    # Step (c)
    # Compute the residuals of the dataset
    resid_variance = 1 - r**2 #

    return pcs, variance_explained, resid_variance#, flatten_D_Euclidean


def isomap_manifold_learning(data,n_neighbors,n_components):

    # T = length of each time series
    Time = np.shape(data)[0]
    # N = dimensionality of the (temperature) state space
    N = np.shape(data)[1]

    # define the fucking model
    embedding = Isomap(n_neighbors=n_neighbors,n_components=n_components,path_method='FW',n_jobs=-1)
    # fit the data
    projected_embedding = embedding.fit_transform(data)

    # Projection of Isomap should be normalized
    pcs_isomap = projected_embedding/np.std(projected_embedding,axis=0)

    # Perfect then the spatial component is the same shit as before
    # Spatial components can be computed as a regression over the data
    components = (1/(Time-1))*np.dot(pcs_isomap.T,data)

    # Now, variance explained?

    # Step (a)
    # Compute the distance matrix D_G
    D_G = embedding.dist_matrix_

    # Step (b)
    # (b.1) Compute the distance matrix in the LOW dimensional embedding using Euclidean distance
    # (b.2) Compute the correlation r between the distance matrix D_G and D_Y
    # (b.3) Compute the residual variance (1 - r^2)

    # Initialize the correlation vector
    r = []

    # We work with symmetric matrices: let's consider only the upper triangular part
    flatten_D_G = D_G[np.triu_indices(D_G.shape[0],k=1)]

    for i in np.arange(1,n_components+1):

        D_Y = cdist(projected_embedding[:,0:i], projected_embedding[:,0:i], 'euclidean')
        flatten_D_Y = D_Y[np.triu_indices(D_Y.shape[0],k=1)]
        r.append(stats.pearsonr(flatten_D_Y,flatten_D_G)[0])

    r = np.array(r)

    # Step (c)
    # Compute the residuals of the dataset
    resid_variance = 1 - r**2 # let's round to 2nd decimal figure

    return pcs_isomap, resid_variance#, flatten_D_G
