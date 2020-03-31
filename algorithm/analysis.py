from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
from scipy.stats import spearmanr
import statsmodels.api as sm
import numpy as np


def standardize_features(x):
    return StandardScaler().fit_transform(x)


def spearmanr_rank(data):
    corr, p_value = spearmanr(data)
    return corr, p_value


def pca_analysis(x, n=2):
    pca = PCA(n_components=n)
    principal_components = pca.fit_transform(x)
    print("pca.pca.explained_variance_|", pca.explained_variance_)
    print("pca.explained_variance_ratio_|", pca.explained_variance_ratio_)
    pca.components_ = np.around(np.asarray(pca.components_), decimals=3)

    np.set_printoptions(suppress=True)
    print("pca.components|", pca.components_)
    return principal_components


def linear_regression(x, y):
    # Note the difference in argument order
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    predictions = model.predict(x)  # make the predictions by the model
    # Print out the statistics
    return model.summary()
