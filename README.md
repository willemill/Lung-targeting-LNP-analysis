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
├── script.py # Main analysis script  
├── requirements.txt # Dependencies  
├── README.md # Project documentation  
├── LICENSE # License file (MIT)  
├── CONTRIBUTING.md # Contribution guidelines  
├── .gitignore # Ignored files  
└── figs/ # Output figures (auto-generated)

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/lung-np-analysis.git
cd lung-np-analysis
pip install -r requirements.txt
```

---

## Usage

Place your dataset (CSV format) in the project root directory.
The default file path in the script is:

```
/Data.csv
```

Run the script:

```
python script.py
```

Results:

Silhouette Score printed in the console.
t-SNE visualizations saved in figs/.

Example Output
t-SNE Clustering.png → visualization of clustered data
t-SNE Efficiency.png → molecules colored by efficiency values
t-SNE Selectivity.png → molecules colored by selectivity values

---

## Dependencies

See requirements.txt for full list.  

Key libraries:  
numpy  
pandas  
matplotlib  
scikit-learn

---

## License

This project is licensed under the MIT License.
