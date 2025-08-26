import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load dataset and create embeddings
df = pd.read_csv('movies.csv')
model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['plot'].tolist(), convert_to_tensor=False)

def search_movies(query, top_n=5):
    """
    Searches for movies based on a query.

    Args:
        query (str): The search query.
        top_n (int): The number of top results to return.

    Returns:
        pandas.DataFrame: A DataFrame with the top N movies, including their titles, plots, and similarity scores.
    """
    query_embedding = model.encode([query], convert_to_tensor=False)
    
    # Calculate cosine similarity
    similarities = cosine_similarity(query_embedding, embeddings)[0]
    
    # Get top N indices
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    
    # Create result DataFrame
    result_df = df.iloc[top_indices].copy()
    result_df['similarity'] = similarities[top_indices]
    
    return result_df

if __name__ == '__main__':
    # Example usage
    search_query = "A spy navigates intrigue in Paris to stop a terrorist plot."
    results = search_movies(search_query, top_n=3)
    print(results)