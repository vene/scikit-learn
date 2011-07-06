"""
Matrix decomposition algorithms
"""

from .nmf import NMF, ProjectedGradientNMF
from .pca import PCA, RandomizedPCA, ProbabilisticPCA, KernelPCA
from .sparse_pca import SparsePCA, dict_learning, dict_learning_online
from .fastica_ import FastICA, fastica
from .dict_learning import DictionaryLearning, DictionaryLearningOnline
from .kmeans_coder import KMeansCoder
