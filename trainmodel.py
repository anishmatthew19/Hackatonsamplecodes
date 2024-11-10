import os
import pandas as pd
import numpy as np
from azure.ai.openai import OpenAIClient
from azure.core.credentials import AzureKeyCredential
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set up Azure OpenAI client
api_key = "YOUR_API_KEY"
endpoint = "https://YOUR_RESOURCE_NAME.openai.azure.com/"
client = OpenAIClient(endpoint=endpoint, credential=AzureKeyCredential(api_key))

def get_text_embedding(text, model="text-embedding-ada-002"):
    # Obtain embedding for a given text
    response = client.embeddings(model=model, input=[text])
    return response["data"][0]["embedding"]

# Example: Load your data (dummy example)
data = pd.DataFrame({
    'transaction_notes': ["Payment delay in March", "On-time payment", "Requested extension"],
    'features': [[1000, 5], [1500, 2], [1200, 3]],  # additional numerical features
    'defaulted': [1, 0, 1]  # target variable
})

# Convert text data into embeddings
data['embedding'] = data['transaction_notes'].apply(get_text_embedding)
data_embeddings = np.array(data['embedding'].to_list())

# Combine with additional features
X = np.hstack((data_embeddings, np.array(data['features'].to_list())))
y = data['defaulted']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model accuracy: {accuracy:.2f}")
