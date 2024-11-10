import openai
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Initialize OpenAI with Azure credentials
openai.api_key = 'your_azure_openai_key'

# Generate embeddings for text features
def get_embeddings(text):
    response = openai.Embedding.create(input=text, engine="text-embedding-ada-002")
    return response['data'][0]['embedding']

# Example data
customer_data = {
    'text': ["customer has been late on payments", "good payment history", "inconsistent income"],
    'income': [50000, 70000, 30000],
    'credit_score': [600, 750, 580],
    'default': [1, 0, 1]
}

# Generate embeddings and combine with other features
customer_data['text_embeddings'] = [get_embeddings(text) for text in customer_data['text']]
X = [list(embedding) + [income, score] for embedding, income, score in zip(customer_data['text_embeddings'], customer_data['income'], customer_data['credit_score'])]
y = customer_data['default']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Model training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Prediction and evaluation
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
