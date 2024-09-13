# Understanding the Impact of Open Source Software Bots: A Comprehensive Taxonomy and Longitudinal Analysis

This repository contains the code, data, and results related to the paper **"Understanding the Impact of Open Source Software Bots: A Comprehensive Taxonomy and Longitudinal Analysis."** The repository is structured into two main parts corresponding to our research questions (RQ1 and RQ2). Each folder includes Jupyter notebooks (`.ipynb`) and Python scripts used to conduct the analysis, along with relevant data and generated results.

## Repository Structure

```
├── RQ1_paper_process/
│   ├── data/
│   └── process.ipynb
├── RQ2_bot_evaluation_process/
│   ├── chart/
│   ├── data/
│   ├── 01account_data_process.ipynb
│   ├── 02process_event_comments_similarity.py
│   ├── 03repo_metric_process.ipynb
│   └── 04rdd_process.ipynb
└── README.md
```
### 1. RQ1: Taxonomy of OSS Bots

**Folder:** `RQ1_paper_process/`

This folder contains the Jupyter notebook and related data for developing the taxonomy of Open Source Software (OSS) Bots. The taxonomy is structured around three primary dimensions: environment, function, and interaction, as outlined in the paper.

**Contents:**
- **`data/`**: Contains data used for bot classification, feature extraction, and final results related to the taxonomy.
- **`process.ipynb`**: Jupyter notebook that processes the data and generates the taxonomy results following the methodology discussed in the paper.

**How to Run:**
1. Ensure that you have a Jupyter environment installed (see Prerequisites below).
2. Open and run the `process.ipynb` notebook in Jupyter.
3. The generated outputs (charts, tables, etc.) will be saved or displayed within the notebook.

### 2. RQ2: Bot Evaluation and RDD Analysis

**Folder:** `RQ2_bot_evaluation_process/`

This folder contains multiple Jupyter notebooks and a Python script for evaluating the impact of OSS Bots on repository metrics, using Regression Discontinuity Design (RDD). The data covers a 24-month period around bot adoption, and the analysis focuses on how bot adoption influences key metrics, such as pull requests, issue handling, and contributor behavior.

**Contents:**
- **`chart/`**: Contains visualizations generated from the analysis, such as charts and graphs.
- **`data/`**: Includes the raw and processed datasets related to repository metrics before and after bot adoption.
- **`01account_data_process.ipynb`**: Jupyter notebook that processes account data related to the repositories.
- **`02process_event_comments_similarity.py`**: Python script that processes event comments and calculates similarity metrics.
- **`03repo_metric_process.ipynb`**: Jupyter notebook that processes repository metrics for further analysis.
- **`04rdd_process.ipynb`**: Jupyter notebook that applies Regression Discontinuity Design (RDD) to analyze the impact of bot adoption on repository metrics.

**How to Run:**
1. Ensure that you have a Jupyter environment installed (see Prerequisites below).
2. Run the Jupyter notebooks in sequence:
    - Start with `01account_data_process.ipynb` to process account data.
    - Use the `02process_event_comments_similarity.py` script to compute similarity metrics.
    - Proceed with `03repo_metric_process.ipynb` to process repository metrics.
    - Finally, run `04rdd_process.ipynb` to perform the RDD analysis.
3. The outputs, including charts and results, will be saved in the `chart/` folder.

### Prerequisites

Ensure you have Jupyter installed on your machine. You can install Jupyter using the following command:

```bash
pip install jupyter
