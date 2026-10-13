import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
df = pd.read_csv("customer_segmentation_100.csv")
#print(df)
X = df[['Age','Annual_Income_k$','Spending_Score']]
model = KMeans(n_clusters=4)
# Training  the model
model.fit(X)
# extraction of the cluster center 
print(model.cluster_centers_)
y_test = [
    [33,90,50]
]
# predict 
result = model.predict(y_test)
print(result)

df['Clusters'] = model.labels_

plt.scatter(df['Annual_Income_k$'], df['Spending_Score'], c=df['Clusters'], s=70)

plt.scatter(model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            marker="X",
            s=250,
            color="black")

plt.show()
