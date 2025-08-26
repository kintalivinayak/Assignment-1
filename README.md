# Movie Semantic Search Assignment

This repository contains my solution for the semantic search on movie plots assignment. The project implements a semantic search engine that can find movies based on plot similarity using natural language queries.

## Project Overview

This assignment demonstrates the implementation of a semantic search system using:
- **SentenceTransformers** (`all-MiniLM-L6-v2`) for creating text embeddings
- **Cosine similarity** for measuring semantic similarity between queries and movie plots
- **Pandas** for data manipulation and results formatting

The search engine can understand the meaning of queries and return relevant movies even when exact keywords don't match.

## Features

- Semantic search functionality that understands context and meaning
- Returns top-N most similar movies with similarity scores
- Comprehensive unit tests to validate functionality
- Clean, documented code with proper error handling

## Prerequisites

- Python 3.9 or higher
- Git (for version control)
- Jupyter Notebook

## Setup

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd movie-search-assignment
   ```

2. Create and activate a virtual environment:
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Jupyter notebook:
   ```bash
   jupyter notebook movie_search_solution.ipynb
   ```

## Repository Structure

```
movie-search-assignment/
├── movie_search.py              # Main Python module with search function
├── movie_search_solution.ipynb  # Jupyter notebook with complete solution
├── movies.csv                   # Dataset with movie titles and plots
├── requirements.txt             # Python dependencies
├── README.md                   # This file
└── tests/
    └── test_movie_search.py    # Unit tests for validation
```

## Testing

Run the unit tests to verify the implementation:

```bash
python -m unittest tests/test_movie_search.py -v
```

All tests should pass, validating:
- Correct output format (DataFrame with proper columns)
- Proper handling of `top_n` parameter
- Similarity scores in valid range (0-1)
- Relevance of search results

## Usage

### In Jupyter Notebook
Open `movie_search_solution.ipynb` and run all cells to see the complete implementation.

### Using the Python Module
```python
from movie_search import search_movies

# Search for movies similar to a query
results = search_movies('spy thriller in Paris', top_n=3)
print(results)
```

### Example Output
```
                title                                               plot  similarity
0           Spy Movie  A spy navigates intrigue in Paris to stop a t...    0.845123
1      Romance in Paris  A couple falls in love in Paris under romant...    0.432156
2        Action Flick  A high-octane chase through New York with exp...    0.321789
```

## Algorithm Details

1. **Text Embedding**: Movie plots and search queries are converted to dense vector representations using the `all-MiniLM-L6-v2` model
2. **Similarity Calculation**: Cosine similarity is computed between the query embedding and all movie plot embeddings
3. **Ranking**: Movies are ranked by similarity score and the top-N results are returned

## Assignment Requirements Met

✅ Implemented semantic search using SentenceTransformers  
✅ Used `all-MiniLM-L6-v2` model for embeddings  
✅ Created comprehensive Jupyter notebook with explanations  
✅ Implemented `search_movies(query, top_n)` function  
✅ All unit tests passing (4/4)  
✅ Clean, commented code  
✅ Proper documentation  

## Author

Assignment completed for AI Systems Development course at IIIT Naya Raipur.
