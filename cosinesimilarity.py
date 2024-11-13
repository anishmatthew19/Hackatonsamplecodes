def cosine_similarity(a, b):
  """
  This function calculates the cosine similarity between two embedding vectors.
  """
  return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(text, model="text-embedding-ada-002"):
  """
  This function retrieves the embedding for a given text using the specified model.
  """
  # Code to call Azure OpenAI API for embedding generation

def search_docs(df, user_query, top_n=4, to_print=True):
  """
  This function searches for documents in the DataFrame based on user query similarity.
  """
  # 1. Get the embedding for the user query
  embedding = get_embedding(user_query)
  # 2. Calculate cosine similarity between the query embedding and each document embedding
  df["similarities"] = df.ada_v2.apply(lambda x: cosine_similarity(x, embedding))
  # 3. Sort documents by similarity in descending order and return the top 'top_n' results
  res = df.sort_values("similarities", ascending=False).head(top_n)
  if to_print:
    print(res)
  return res

# Example usage: Find documents similar to the query "Can I get information on cable company tax revenue?"
user_query = "Can I get information on cable company tax revenue?"
res = search_docs(df_bills, user_query, top_n=4)
