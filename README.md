# Movie Plot Semantic Search Project

This repository presents my implementation of a semantic search system for discovering movies based on plot similarity through natural language queries.

## Project Description

This project showcases the development of a semantic search engine utilizing:
- **SentenceTransformers** (specifically the `all-MiniLM-L6-v2` model) for generating text embeddings
- **Cosine similarity** for computing semantic relationships between user queries and movie storylines
- **Pandas** for data processing and result presentation

The system can comprehend query meanings and retrieve relevant films even without exact keyword matches.

## Key Capabilities

- Context-aware semantic search that interprets meaning beyond literal text matching
- Delivers top-N most relevant movies along with similarity confidence scores  
- Complete test suite ensuring functionality validation
- Well-structured, documented codebase with robust error management

## System Requirements

- Python version 3.9 or newer
- Git for repository management
- Jupyter Notebook environment

## Installation Guide

1. Download the repository:
   ```bash
   git clone <your-repository-url>
   cd movie-search-assignment
   ```

2. Set up and activate a virtual environment:
   - Windows users:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - macOS/Linux users:
     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the Jupyter notebook:
   ```bash
   jupyter notebook movie_search_solution.ipynb
   ```

## Project File Organization

```
movie-search-assignment/
├── movie_search.py              # Core Python module containing search functionality
├── movie_search_solution.ipynb  # Complete solution in Jupyter notebook format
├── movies.csv                   # Movie dataset containing titles and plot descriptions
├── requirements.txt             # List of Python package dependencies
├── README.md                   # Project documentation (this file)
└── tests/
    └── test_movie_search.py    # Comprehensive unit tests for verification
```

## Running Tests

Execute unit tests to confirm implementation correctness:

```bash
python -m unittest tests/test_movie_search.py -v
```

All tests are designed to pass, confirming:
- Appropriate output structure (DataFrame with required columns)
- Correct handling of the `top_n` parameter
- Valid similarity score ranges (between 0 and 1)
- Meaningful search result relevance

## How to Use

### Within Jupyter Notebook
Launch `movie_search_solution.ipynb` and execute all cells to view the full implementation.

### Direct Python Module Usage
```python
from movie_search import search_movies

# Find movies matching a specific query
results = search_movies('spy thriller in Paris', top_n=3)
print(results)
```

### Sample Results
```
                title                                               plot  similarity
0           Spy Movie  A spy navigates intrigue in Paris to stop a t...    0.845123
1      Romance in Paris  A couple falls in love in Paris under romant...    0.432156
2        Action Flick  A high-octane chase through New York with exp...    0.321789
```

## Technical Implementation

1. **Vector Embedding**: Both movie plots and search queries are transformed into high-dimensional vector representations using the `all-MiniLM-L6-v2` transformer model
2. **Similarity Measurement**: Cosine similarity metrics are calculated between query vectors and all movie plot vectors
3. **Result Ranking**: Films are ordered by similarity scores, returning the highest-scoring N results

## Completed Assignment Criteria

✅ Successfully implemented semantic search using SentenceTransformers framework  
✅ Utilized the specified `all-MiniLM-L6-v2` embedding model  
✅ Developed detailed Jupyter notebook with clear explanations  
✅ Built functional `search_movies(query, top_n)` method  
✅ Achieved 100% test success rate (4/4 tests passing)  
✅ Maintained clean, well-commented code structure  
✅ Provided thorough project documentation  

## Credits

Project developed for the AI Systems Development coursework at IIIT Naya Raipur.
