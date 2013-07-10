"""
=====================================================
Applying Spectral Biclustering to a generated dataset
=====================================================

This example demonstrates how to generate a checkerboard dataset for
the Spectral Biclustering algorithm and fit it.

The row and column labels assigned to biclusters may not match the
original row and column labels, which is why the fitted checkerboard
may not look exactly like the original. The appropriate row and column
exchanges would make them look more similar.

"""
print(__doc__)

# Author: Kemal Eren <kemal@kemaleren.com>
# License: BSD 3 clause

import numpy as np
import pylab as pl

from sklearn.datasets import make_checkerboard
from sklearn.bicluster import SpectralBiclustering

n_clusters = (4, 3)
data, row_labels, column_labels = make_checkerboard(
    shape=(300, 300), n_clusters=n_clusters, noise=10,
    shuffle=True, random_state=0)
model = SpectralBiclustering(n_clusters=n_clusters, method='log')
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
