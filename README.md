# Algerian Forest Fire Prediction
This project was my first experience developing and deploying a complete machine learning application.

its basic machine learning web application that predicts the **Fire Weather Index (FWI)** using meteorological and environmental parameters from the **Algerian Forest Fires Dataset**. The application is built with **Flask** and powered by a **Ridge Regression** model trained using **scikit-learn**.

 **Live Demo**: https://algerian-fire-risk-predictor.onrender.com

## Overview

Wildfires are influenced by several environmental factors such as temperature, humidity, wind speed, and rainfall. This project leverages machine learning to estimate the **Fire Weather Index (FWI)**, an important indicator used in wildfire risk assessment.

Users can input real-world weather conditions through a clean and interactive web interface, and the trained model instantly predicts the corresponding Fire Weather Index.

---

## Features

- Predicts the Fire Weather Index (FWI)
- Machine Learning model built using Ridge Regression
- Data preprocessing using StandardScaler
- Interactive Flask web application
- Responsive and modern user interface
- Real-time predictions
- Deployed on Render

---

## Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-learn
- Ridge Regression
- StandardScaler

### Data Processing
- Pandas
- NumPy

### Frontend
- HTML5
- CSS3

### Deployment
- Render

## Installation

Clone the repository

```bash
git clone https://github.com/akshita568/FireIndexPred.git
```

Move into the project directory

```bash
cd FireIndexPred
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Once the server starts, open your browser and visit:
http://127.0.0.1:5000


## Deployment

The application is deployed using **Render**.

Live Website:

https://algerian-fire-risk-predictor.onrender.com

---

This project uses the **Algerian Forest Fires Dataset**, which contains meteorological observations collected from two regions in Algeria:
- Bejaia
- Sidi Bel-Abbes
