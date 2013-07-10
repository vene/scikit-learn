"""
======================================================
Applying Spectral Co-Clustering to a generated dataset
======================================================

This example demonstrates how to generate a dataset for the Spectral
Co-Clustering algorithm and fit it.

"""
print(__doc__)

# Author: Kemal Eren <kemal@kemaleren.com>
# License: BSD 3 clause

import numpy as np
import pylab as pl

from sklearn.datasets import make_biclusters
from sklearn.bicluster import SpectralCoclustering

data, row_labels, column_labels = make_biclusters(
    shape=(300, 300), n_clusters=5, noise=10,
    shuffle=True, random_state=0)

model = SpectralCoclustering(n_clusters=5)
model.fit(data)

fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]

pl.matshow(data[np.argsort(row_labels)]
               [:, np.argsort(column_labels)],
           cmap=pl.cm.Blues)
pl.title("Original dataset")

pl.matshow(data, cmap=pl.cm.Blues)
pl.title("Shuffled dataset")

pl.matshow(fit_data, cmap=pl.cm.Blues)
pl.title("Rearranged to show biclusters")

pl.show()
