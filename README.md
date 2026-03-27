---
title: "KBS Pneumonia Diagnosis"
emoji: "🩺"
colorFrom: "blue"
colorTo: "red"
sdk: docker
pinned: false
---

# 🩺 Hybrid Knowledge-Based Pneumonia Diagnosis System

This system uses a combination of rule-based reasoning and AI-based X-ray analysis to provide explainable risk diagnoses for pneumonia.

## 🚀 How to Run Locally

1.  **Clone the Repository**
2.  **Install Requirements**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run with Streamlit**
    ```bash
    streamlit run app.py
    ```

## 🤖 AI Model (Simulation Mode)

This Space currently runs in **Simulation Mode** if the pre-trained `pneumonia_model.h5` is not found. To use the real model:
1.  Train it locally using `python3 train.py`.
2.  Add the `pneumonia_model.h5` file and push to GitHub.
