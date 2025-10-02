# Lung Targeting Nanoparticle Analysis

This repository contains a Python script for analyzing **lung-targeting nanoparticles (NPs)** using clustering and dimensionality reduction techniques.  
It applies **K-means clustering**, **t-SNE visualization**, and **silhouette scoring** to evaluate molecular features relevant to NP selectivity and efficiency.

---

## Features
- Preprocesses input data (scales numeric features, removes labels for clustering).
- Runs **K-means clustering** with adjustable number of clusters.
- Evaluates cluster quality with **silhouette score**.
- Performs **t-SNE dimensionality reduction** for visualization.
- Generates publication-ready **cluster plots** for different molecular features.

---

## Repository Structure
├── main.py # Main analysis script
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── LICENSE # License file (MIT)
├── .gitignore # Ignored files
└── figs/ # Output figures (auto-generated)
