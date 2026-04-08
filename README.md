# ICDF EDA Streamlit Template

https://advancededaufs-n4safytukywgz7ixlg6srr.streamlit.app/

A production-grade **Exploratory Data Analysis (EDA) and Streamlit deployment template** developed for reproducible analytics workflows within the **Interdisciplinary Centre for Digital Futures (ICDF), University of the Free State (UFS)**.

This repository is designed to support **research-grade, teaching-oriented, and operational analytics pipelines**, enabling rapid movement from **Google Colab experimentation** to **interactive Streamlit deployment**.

The template aligns with ICDF principles of:

* reproducible science
* transparent analytics
* Ubuntu-centred AI ethics
* responsible data governance
* educational reusability
* modular deployment

It is suitable for **business analytics, computational infodemiology, SASL/HLT datasets, financial intelligence, social listening, anomaly detection, and multilingual AI pipelines**.

---

## Institutional Alignment

This template was developed in support of the **Interdisciplinary Centre for Digital Futures (ICDF)** at the **University of the Free State (UFS)**.

The repository reflects the centre’s commitment to:

* inclusive AI innovation
* multilingual and multimodal analytics
* digital transformation research
* ethical data science in emerging contexts
* open science for African scholarship

All derivative academic and institutional use should explicitly acknowledge **ICDF and UFS**.

---

## Repository Structure

```bash
eda-streamlit-icdf/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── eda_pipeline.ipynb
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── diagnostics.py
│   ├── visualisations.py
│   └── utils.py
│
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── reports/
│
├── assets/
│   └── dashboard_preview.png
│
└── docs/
    └── methodology.md
```

---

## Core Features

### Reproducible EDA

* automated descriptive statistics
* null value profiling
* duplicate detection
* schema inference
* outlier diagnostics
* feature drift screening
* imbalance diagnostics
* anomaly summaries

### Research-Grade Visualisation

* histograms
* boxplots
* violin plots
* KDE distributions
* correlation heatmaps
* feature interaction plots
* temporal trend diagnostics
* panel data safe aggregation plots
* rolling windows
* anomaly overlays

### Streamlit Deployment

* drag-and-drop CSV upload
* dynamic feature filtering
* automated chart rendering
* downloadable outputs
* configurable diagnostics panels
* publication-ready export figures

---

## Ethical and Governance Principles

This repository follows **Ubuntu-informed responsible AI and analytics governance**.

### Principles

* fairness and representational inclusion
* multilingual accessibility where applicable
* explainable transformations
* human-in-the-loop validation
* transparent preprocessing
* protection against harmful inferential bias
* POPIA-aligned data stewardship

For sensitive datasets (health, education, finance, sign language corpora), users should ensure compliance with:

* institutional ethics approvals
* UFS AI policy
* POPIA
* relevant data sharing agreements

---

## Quick Start

### 1. Clone

```bash
git clone https://github.com/ICDF-UFS/eda-streamlit-icdf.git
cd eda-streamlit-icdf
```

### 2. Install

```bash
pip install -r requirements.txt
```

### 3. Run

```bash
streamlit run app.py
```

---

## Research and Teaching Use Cases

This repository is designed for:

* honours and masters student projects
* doctoral proof-of-concept analytics
* SASL corpus quality diagnostics
* financial decision intelligence dashboards
* computational infodemiology pipelines
* social stress indicator validation
* digital capability index exploration
* multilingual HLT preprocessing
* business transformation analytics

---

## Deployment Pathways

### Streamlit Community Cloud

Recommended for rapid prototypes and student demonstrations.

### Institutional Servers

Suitable for:

* UFS web nodes
* ICDF internal servers
* protected faculty deployments
* reverse proxy analytics dashboards

### HPC and Scalable Research

Recommended stack:

* Docker
* Kubernetes
* Slurm orchestration
* UFS HPC GPU/CPU nodes
* scheduled batch preprocessing

---

## Reproducibility Standards

To support academic integrity and reproducibility:

* preserve raw data separately
* version preprocessing scripts
* log package versions
* export figures deterministically
* use notebook checkpoints
* document assumptions in `/docs`
* link outputs to manuscript figures where possible

Recommended citation in academic outputs:

> Combrink, H. ICDF EDA Streamlit Template. Interdisciplinary Centre for Digital Futures, University of the Free State.

---

## Future Extensions

Planned advanced modules include:

* explainable AI with SHAP
* reinforcement learning diagnostics
* multilingual RAG ingestion
* SASL video feature analytics
* real-time API ingestion
* netCDF weather analytics
* Looker Studio connectors
* automated model cards
* drift monitoring

---

## Licence and Use

Recommended licence:

**CC BY-NC-SA 4.0** for academic and non-commercial use.

Commercialisation, institutional redistribution, or derivative governance frameworks should involve **ICDF/UFS acknowledgement and formal permission where required**.

---

## Contact

**Dr Herkulaas Combrink**
Co-Director, Interdisciplinary Centre for Digital Futures
University of the Free State
Email: [CombrinkHM@ufs.ac.za](mailto:CombrinkHM@ufs.ac.za)

For collaborations, institutional deployment, or student supervision extensions, please contact the ICDF team.
