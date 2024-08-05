import pandas as pd
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler


def run_tsne(feature_matrix, labels, perp, names):
    # Initaite model with desired perameters
    model = TSNE(n_components=2, perplexity=perp, n_iter=5000, n_iter_without_progress=500)
    # Fit data to model
    tsne_data = model.fit_transform(feature_matrix)
    tsne_df = pd.DataFrame(data=tsne_data, columns=['Dim 1', 'Dim 2'])
    # label data points
    tsne_df['labels'] = labels
    # Visualize the clustered data
    plt.scatter(data=tsne_df, x='Dim 1', y='Dim 2', c='labels', cmap='jet')
    plt.title(f't_SNE {names}')
    plt.colorbar()
    plt.show()


def run_analysis(csv_file, label_column):
    # read in data from CSV and isolate features
    data = pd.read_csv(csv_file)
    # remove labels from the data set
    features = data.drop(columns=[label_column])
    # generate labels
    names = features.keys()
    # create and standardize features matrix
    input_features_matrix = features.values
    input_features_matrix = StandardScaler().fit_transform(input_features_matrix)
    # run t-SNE with different labels
    for ii in range(0, 19, 1):
        run_tsne(input_features_matrix, features.iloc[:, ii], 35, names[ii])
