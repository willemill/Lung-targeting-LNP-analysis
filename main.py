# Written By: William Miller
# Date: 2024-10-29
# Description: This script analyzes lung targeting NPs via clustering and dimensionality reduction techniques.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE

def load_data(file_path):
    data = pd.read_csv(file_path)
    data_numeric = data.select_dtypes(include=[np.number])
    data_included = data_numeric.drop(['Selectivity', 'Efficiency'], axis=1)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data_included)
    return data_scaled, data_numeric

def run_kmeans(data, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(data)
    return clusters

def silhouette_analysis(data, clusters):
    return silhouette_score(data, clusters)

def plot_clusters(data, clusters, title, xlabel, ylabel, map):
    plt.figure(figsize=(10, 6))
    plt.scatter(data[:, 0], data[:, 1], c=clusters, cmap=map, s=50, vmin=min(clusters), vmax=max(clusters))
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()
    plt.savefig(f"figs/{title}.png")
    plt.close()

def run_tsne(data):
    tsne = TSNE(n_components=2, random_state=42)
    return tsne.fit_transform(data)


if __name__ == "__main__":
    file_path = "/Data.csv"
    data, unscaled_data = load_data(file_path)
    
    TSNE_data = run_tsne(data)
    TSNE_clusters = run_kmeans(TSNE_data, n_clusters=23)
    TSNE_silhouette = silhouette_analysis(TSNE_data, TSNE_clusters)
    
    print(f"t-SNE Silhouette Score: {TSNE_silhouette}")
    
    names = ["1 amine",	"one tails", "two tails", "three tails", "four tails",	"over 5 tails",
            "with double bond", "with ester bond",	"with branch", "with hydroxy group", "with cycle structure",
            "with phenyl group", "Carbon number", "moelcule weight over 500",	"Efficiency", "Selectivity", "cLogP", "CMR"
            ]
    
    for i in range(unscaled_data.shape[1]):
        labels = unscaled_data.iloc[:, i]
        name = names[i]
        plot_clusters(TSNE_data, labels, f"t-SNE {name}", "t-SNE Component 1", "t-SNE Component 2", "turbo")
    
    plot_clusters(TSNE_data, TSNE_clusters, "t-SNE Clustering", "t-SNE Component 1", "t-SNE Component 2", "tab20")
