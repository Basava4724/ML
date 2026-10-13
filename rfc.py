import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv("amazon_reviews_100_mixed.csv")
#print(df)
print(df.groupby("Sentiment")["Sentiment"].count())

X = df['Review']

y = df['Sentiment']

cvj = CountVectorizer()
X_vectorized = cvj.fit_transform(X)
#print(X_vectorized)
df_copy = df.copy()
df['original_sentiment_label'] = df_copy['Sentiment']

# factorization of sentiment column
df['Sentiment'] = pd.factorize(df['Sentiment'])[0]
y_train = df['Sentiment']
print(df.groupby(['original_sentiment_label','Sentiment'])['Sentiment'].count())
# Training the model
model = RandomForestClassifier()
model.fit(X_vectorized,y_train)

# prepare test comments
comment = "Packaging was good And highly recommended "
X_test = cvj.transform([comment])
result = model.predict(X_test)
print(result)
