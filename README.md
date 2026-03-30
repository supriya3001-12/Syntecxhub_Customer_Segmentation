# Syntecxhub Customer Segmentation Project

## 📌 Project Overview
This project is part of my Data Science internship at **Syntecxhub**. The objective is to perform **Customer Segmentation** using the **K-Means Clustering** algorithm. By analyzing a dataset of mall customers, we identify distinct groups based on their age, annual income, and spending scores to help the business create targeted marketing strategies.

## 📊 Business Problem
Malls often have a diverse customer base. A "one-size-fits-all" marketing approach is inefficient. This project solves that by:
1. Identifying who the high-value customers are.
2. Understanding the spending patterns of different income groups.
3. Providing data-driven insights for promotional campaigns.

## 🛠️ Technical Stack
- **Language:** Python 3.12
- **Libraries:** - `Pandas`: Data manipulation and analysis.
  - `Matplotlib` & `Seaborn`: Data visualization.
  - `Scikit-learn`: Machine learning (K-Means & StandardScaler).

## 🚀 Methodology
1. **Data Preprocessing**: Handled the dataset and normalized features using `StandardScaler` to ensure the clustering algorithm performs accurately.
2. **The Elbow Method**: Ran the K-Means algorithm for $k$ values from 1 to 10 to find the "elbow point," which was determined to be **5 clusters**.
3. **Model Training**: Applied the K-Means algorithm with 5 clusters.
4. **Cluster Profiling**: Analyzed the mean values of each group to understand their behavior.

## 📈 Key Results
The customers were segmented into 5 distinct categories:
- **VIPs**: High Income, High Spending Score.
- **Target Group**: Middle Income, Middle Spending Score.
- **Impulse Buyers**: Low Income, High Spending Score.
- **Sensible Spenders**: High Income, Low Spending Score.
- **Budget Conscious**: Low Income, Low Spending Score.

## 📁 Repository Structure
- `clustering.py`: Main Python script containing the code.
- `Mall_Customers.csv`: The input dataset.
- `Final_Customer_Segmentation_Report.csv`: The output file with cluster labels assigned to each customer.
- `README.md`: Project documentation.

## 🏁 Conclusion
The project successfully segments the mall's customer base into 5 actionable groups, fulfilling the requirements for **Syntecxhub Project-1**.
