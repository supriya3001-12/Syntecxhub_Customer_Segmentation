import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Load data
df = pd.read_csv('Mall_Customers.csv')

# 2. Scale Features (Requirement from your slide)
# We use Annual Income and Spending Score
X = df.iloc[:, [3, 4]].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Elbow Method (Requirement from your slide)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 5))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.show() # TAKE A SCREENSHOT OF THIS FOR YOUR REPORT

# 4. K-Means (Applying k=5 based on standard elbow results)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)

# 5. Visualize (Requirement from your slide)
plt.figure(figsize=(10, 7))
sns.scatterplot(x=X[y_kmeans == 0, 0], y=X[y_kmeans == 0, 1], s=100, label='Cluster 1')
sns.scatterplot(x=X[y_kmeans == 1, 0], y=X[y_kmeans == 1, 1], s=100, label='Cluster 2')
sns.scatterplot(x=X[y_kmeans == 2, 0], y=X[y_kmeans == 2, 1], s=100, label='Cluster 3')
sns.scatterplot(x=X[y_kmeans == 3, 0], y=X[y_kmeans == 3, 1], s=100, label='Cluster 4')
sns.scatterplot(x=X[y_kmeans == 4, 0], y=X[y_kmeans == 4, 1], s=100, label='Cluster 5')
plt.title('Customer Segments')
plt.show() # TAKE A SCREENSHOT OF THIS FOR YOUR REPORT

# 6. Save Labels (Requirement from your slide)
df['Cluster'] = y_kmeans
df.to_csv('Final_Submission_Report.csv', index=False)
print("File 'Final_Submission_Report.csv' created. Download it from the folder icon on the left!")