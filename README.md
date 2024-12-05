# Intrusion Detection Proxy Server with Clustering

This project is a proxy server application that uses **clustering** techniques to detect potential intrusions in incoming HTTP requests. It leverages **PyCaret** for clustering analysis and extracts features from HTTP paths to classify requests as potentially malicious or benign.

## Features
- Extracts features from HTTP paths, such as quotes, dashes, and bad keywords.
- Uses **K-Means Clustering** to classify HTTP requests into clusters.
- Detects intrusions based on the cluster assignment.
- Implements a proxy server to forward or block requests based on clustering results.

## Requirements

- Python 3.8 or later
- The following Python libraries:
  - `pandas`
  - `numpy`
  - `pycaret`
  - `scikit-learn`
  - `urllib3`
  - `http.server` (built-in with Python)

Refer to the `requirements.txt` file for the full list of dependencies.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-name.git
   cd your-repository-name
