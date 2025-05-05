# DNA-Sequence-Analysis-and-API-Development


## File Descriptions

| File                    | Description |
|-------------------------|-------------|
| `main.py`               | The entry point of the FastAPI application. It initializes the app and includes all API routes using the router. |
| `router.py`             | Contains all the route logic including the `/upload-csv/` endpoint which reads, validates, and stores CSV data in memory and writes it to a JSON file. |
| `llm.py`                | Here the logic is defined to use the llm integration for ask_me_anything fucntionality |
| `dna_generation.py`     | this function holds responsible to generate the relevant dna sequence based on the given id |
| `llm_context.txt`       | this txt file defines the context provided to llm to answer the users question regarding the application |
| `utils.py`              | Utility functions for calculating the similarity score between a dna pair |
| `preprocess.ipynb`      | this nb defines the basic preprocessing steps to clean the data before processing it further |
