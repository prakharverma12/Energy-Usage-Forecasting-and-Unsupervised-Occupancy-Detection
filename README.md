
# Energy Forecasting and Unsupervised Occupancy Detection for Office Spaces

## 🏁 Overview

This project develops advanced hourly energy forecasting pipelines for office spaces by leveraging sensor data, state‑of‑the‑art machine learning, and deep learning methods. It achieves highly accurate forecasting and actionable optimization for HVAC and energy usage.

---

## ⚡️ Features

* ✅ **Advanced Forecasting Models**:

  * Developed pipelines using **XGBoost**, **LSTM**, and **ensemble stacking** achieving an RMSE of **0.0594**.
  * Reduced forecasting error by **45%** compared to baseline linear regression.

* 🔥 **Integrated Sensor Inputs**:

  * Incorporated **CO levels**, **Relative Humidity (RH)**, **temperature**, and **lighting load** for precise forecasting.

* 📊 **Energy‑IAQ Analysis**:

  * Identified **plug load** and **HVAC usage** as dominant contributors (\~**63–69%**) to daily energy variability, aligning with state‑of‑the‑art research.

* ❄️ **Optimized HVAC Control**:

  * Developed **demand‑controlled ventilation** strategies based on CO thresholds, yielding an estimated **25%** reduction in HVAC energy usage during the day.

---

## 🛠️ Technologies

* **Python 3.8+**
* **scikit‑learn**, **XGBoost**, **Keras / TensorFlow**
* **Pandas**, **NumPy** for data preprocessing
* **Matplotlib**, **Seaborn** for plotting and data exploration
* Time‑series forecasting & ensemble learning
* HVAC optimization and energy modeling

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or later
* Install required packages:

  ```
  pip install -r requirements.txt
  ```

### Installation

```bash
git clone https://github.com/your-username/energy-forecasting.git
cd energy-forecasting
pip install -r requirements.txt
```

### Usage

* **Train forecasting model**:

  ```bash
  python run_forecast.py
  ```
* **Run HVAC optimization**:

  ```bash
  python optimize_hvac.py
  ```

---

## 📊 Results

* ✅ RMSE: **0.0594** for hourly energy prediction
* ✅ Reduced error by **45%** vs. baseline linear regression
* ✅ Identified **63–69%** daily variability explained by plug load and HVAC
* ✅ Achieved \~**25%** estimated HVAC energy savings via CO‑based demand‑controlled ventilation

---

## 🏆 Impact

This project empowers facilities and energy managers with precision forecasting and actionable optimization strategies, aligning with state‑of‑the‑art research to make buildings smarter, more sustainable, and cost‑effective.

