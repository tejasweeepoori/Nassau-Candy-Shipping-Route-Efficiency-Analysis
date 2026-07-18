# 🚚 Nassau Candy Logistics Analytics

## Factory-to-Customer Shipping Route Efficiency Analysis

---

## 📌 Project Overview

This project focuses on analyzing the **factory-to-customer shipping efficiency** of **Nassau Candy Distributor**, a national candy distributor operating across multiple regions in the United States.

The objective is to transform raw shipment data into meaningful logistics insights by identifying:

- Efficient shipping routes
- Delayed routes
- Regional bottlenecks
- Ship mode performance
- Operational improvement opportunities

The project uses **Python, Exploratory Data Analysis (EDA), Data Visualization, and Streamlit Dashboarding** to create a data-driven logistics intelligence system.

---

# 🎯 Problem Statement

Nassau Candy Distributor has large amounts of order and shipment data but lacks visibility into logistics performance.

The organization needs answers to:

- Which factory-to-customer routes are most efficient?
- Which routes experience frequent delays?
- How does shipping performance vary by region and state?
- Which shipping modes provide better delivery efficiency?
- Where are the major operational bottlenecks?

This project provides route-level analysis to support better supply chain decisions.

---

# 📂 Dataset Description

The dataset contains order, customer, product, shipment, and financial information.

### Dataset Features:

| Feature | Description |
|---|---|
| Row ID | Unique row identifier |
| Order ID | Unique order identifier |
| Order Date | Date when order was placed |
| Ship Date | Date when product was shipped |
| Ship Mode | Shipping method |
| Customer ID | Customer identifier |
| Country/Region | Customer country |
| City | Customer city |
| State/Province | Customer state |
| Region | Customer region |
| Product ID | Product identifier |
| Product Name | Product details |
| Division | Product category |
| Sales | Total sales value |
| Units | Quantity ordered |
| Cost | Manufacturing cost |
| Gross Profit | Profit generated |

---

# 🛠️ Technologies Used

## Programming Language

- Python

## Python Libraries

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit

## Tools

- Jupyter Notebook
- Anaconda
- GitHub

---

# 🔄 Project Workflow

```
Dataset Collection
        |
        ↓
Data Cleaning
        |
        ↓
Data Preprocessing
        |
        ↓
Feature Engineering
        |
        ↓
Route Efficiency Analysis
        |
        ↓
Exploratory Data Analysis
        |
        ↓
Dashboard Development
        |
        ↓
Business Insights
```

---

# 🧹 Data Preprocessing

The following preprocessing techniques were performed:

- Checked missing values
- Removed duplicate records
- Converted date columns into datetime format
- Removed invalid shipment records
- Standardized geographic information
- Created new analytical features

---

# ⚙️ Feature Engineering

## Shipping Lead Time

Shipping duration was calculated as:

```
Lead Time = Ship Date - Order Date
```

Additional features created:

- Factory location
- Factory-to-customer route
- Shipment status
- Delay classification

---

# 🏭 Factory Mapping

Products were assigned to manufacturing factories based on product information.

| Factory | Location |
|---|---|
| Lot's O' Nuts | Arizona, USA |
| Wicked Choccy's | Georgia, USA |
| Sugar Shack | Minnesota, USA |
| Secret Factory | Illinois, USA |
| The Other Factory | Tennessee, USA |

---

# 📊 Key Performance Indicators (KPIs)

The following metrics were analyzed:

## Shipping Lead Time

Average number of days required for shipment.

## Route Volume

Total number of shipments handled by each route.

## Delay Frequency

Percentage of shipments exceeding the defined delivery threshold.

## Route Efficiency Score

Ranking routes based on shipping performance.

---

# 📈 Exploratory Data Analysis

## Route Performance Analysis

Analyzed:

- Top 10 fastest routes
- Bottom 10 slowest routes
- Factory-to-state shipping performance

---

## Geographic Analysis

Identified:

- High-delay regions
- Shipment concentration areas
- Operational bottlenecks

---

## Ship Mode Analysis

Compared shipping efficiency among:

- Standard Class
- First Class
- Second Class
- Same Day Shipping

---

# 📱 Streamlit Dashboard

An interactive web dashboard was developed using Streamlit.

## Dashboard Modules

### 1. Route Efficiency Overview

Features:

- Average lead time by route
- Best performing routes
- Worst performing routes

---

### 2. Geographic Shipping Analysis

Features:

- State-wise shipping efficiency
- Regional bottleneck visualization
- Shipment distribution

---

### 3. Ship Mode Comparison

Features:

- Lead time comparison
- Shipping method performance analysis

---

### 4. Interactive Filters

Users can filter results using:

- Date range
- Region
- State
- Ship Mode
- Lead-time threshold

---

# 📁 Project Structure

```
Nassau-Candy-Logistics-Analytics

│
├── data
│   └── Nassau_Candy_Distributor.csv
│
├── notebooks
│   └── Shipping_Route_Analysis.ipynb
│
├── app.py
│
├── clean_shipping_data.csv
│
├── route_analysis.csv
│
├── requirements.txt
│
└── README.md
```

---

# 🔍 Key Insights

The project provides insights into:

- Most efficient factory-to-customer routes
- Routes causing delivery delays
- Regional shipping performance
- Impact of shipping modes
- Supply chain improvement opportunities

---

# 🚀 Future Improvements

Future enhancements include:

- Machine learning model for delay prediction
- Automated route optimization
- Real-time logistics monitoring
- GIS-based shipping visualization
- Cost optimization models
- Predictive supply chain analytics

---

# 👨‍💻 Author

**Tejaswee Epoori**

Robotics and Artificial Intelligence Engineering Student

Amrita Vishwa Vidyapeetham, Bengaluru

---

## ⭐ Project Highlights

✅ Data Cleaning  
✅ Feature Engineering  
✅ Logistics Analytics  
✅ Route Performance Analysis  
✅ Data Visualization  
✅ Streamlit Dashboard  
✅ Supply Chain Insights  

---

⭐ If you found this project useful, consider giving it a star!
