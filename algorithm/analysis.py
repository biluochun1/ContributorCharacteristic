from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from sklearn.decomposition import PCA
from scipy.stats import spearmanr
import statsmodels.api as sm


def standardize_features(x):
    return StandardScaler().fit_transform(x)


def pca_analysis(x, n=2):
    pca = PCA(n_components=n)
    principal_components = pca.fit_transform(x)
    print(pca.explained_variance_ratio_)
    # print(pca.n_features_)
    # print(len(principal_components))
    return principal_components


def spearmanr_rank(data):
    corr, p_value = spearmanr(data)
    return corr, p_value


def linear_regression(x, y):
    # Note the difference in argument order
    # x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    predictions = model.predict(x)  # make the predictions by the model
    # Print out the statistics
    return model.summary()

