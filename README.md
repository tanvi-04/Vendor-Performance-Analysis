🏭 Vendor Performance Analysis

A complete data analytics project to evaluate vendor performance using purchase, price, inventory, and invoice data.
It builds a pipeline from data ingestion → transformation → analysis → visualization, helping businesses identify cost-efficient and reliable suppliers.

🔍 Overview

This project provides an end-to-end workflow to:
  -Load raw CSV files into an SQLite database
  -Compute vendor-wise KPIs (spend, profit, freight cost, turnover)
  -Visualize cost trends, delivery reliability, and sales ratios
  -Support data-driven vendor management decisions

🧱 Tech Stack

Languages: Python 3.10+
Libraries: Pandas · NumPy · Matplotlib · Seaborn · SQLAlchemy
Database: SQLite
Interface: Jupyter Notebook

📂 Folder Structure
<img width="1120" height="636" alt="image" src="https://github.com/user-attachments/assets/e368afbb-fd23-41d1-b9df-6e5c9cc22db0" />

⚙️ Setup & Installation

1. Clone the repository
<img width="544" height="108" alt="image" src="https://github.com/user-attachments/assets/9a9ecbc0-a788-4ebc-b0ac-15d9973c703b" />

2. Install required libraries
<img width="980" height="72" alt="image" src="https://github.com/user-attachments/assets/0517a19d-bd69-4d36-b390-4f7b4e4aec4c" />

3. Load data into the database
<img width="426" height="78" alt="image" src="https://github.com/user-attachments/assets/55507f9c-1755-4425-9c47-de1b78fe596a" />

4. Generate vendor performance summary
<img width="426" height="78" alt="image" src="https://github.com/user-attachments/assets/3ca42f97-bafb-49f8-94ec-85a6cd889837" />

5. Explore results
<img width="320" height="84" alt="image" src="https://github.com/user-attachments/assets/6ceccd42-32bd-4b0d-9aa0-33991c4468d1" />

Then open:
- Exploratory_Data_Analysis.ipynb → Data cleaning and visualization
- Vendor Performance Analysis.ipynb → Consolidated analysis and insights


📊 Workflow Summary
1️⃣ Data Ingestion
  - Reads multiple CSVs and loads them into an SQLite database.
  - Uses SQLAlchemy for fast and structured ingestion.
  - Handles missing or invalid records gracefully.
    
2️⃣ Data Transformation
  - Joins purchase, price, and invoice data.
  - Computes financial and operational KPIs such as:
  - Total Purchase & Sales
  - Gross Profit and Profit Margin
  - Freight Cost per Vendor
  - Inventory Turnover Rate

3️⃣ Analysis & Visualization
  - Correlation heatmaps for purchase and delivery metrics
  - Vendor ranking charts by total cost and margin
  - Inventory utilization trends (begin vs. end)
  - Outlier detection for freight and purchase price

📈 Key Insights
- Identified high-performing vendors with consistent delivery times
- Highlighted cost fluctuations across brands
- Quantified freight contribution to total procurement cost
- Mapped purchase volume to profit margins for optimization

Visualizations (generated in notebooks):
- 📉 Vendor cost trend over time
- 🧩 Correlation heatmap of quantity, cost, and freight
- 📦 Inventory change (begin vs. end)
- 🏆 Top 10 vendors by revenue contribution

🚀 Highlights

✅ Modular, script-based architecture
✅ Clean database-driven design
✅ Reproducible analysis via Jupyter notebooks
✅ Easy to extend for larger procurement datasets

🔮 Future Enhancements
- Automated performance report generation (PDF / dashboard)
- Streamlit or Power BI integration
- Predictive vendor risk scoring
- Real-time data ingestion pipeline



















