# Week 1: LLM Fundamentals - Exercises

This folder contains hands-on Python exercises for the following foundational topics in AI engineering:

## Topics Covered
- Hallucination
- Tokenization
- Vectorization
- Attention
- Few-Shot Prompting
- Retrieval-Augmented Generation (RAG)
- Vector Database Search

## How to Run Each Exercise

1. Make sure you have followed the setup instructions in the main README (virtual environment, requirements, .env file).
2. Each script is self-contained and can be run individually:

```powershell
python ex2_hallucination.py
python ex3_tokenization.py
python ex4_vectorization.py
python ex5_attention.py
python ex6_few_shot.py
python ex7_rag.py
python ex8_vector_db.py
```

- For OpenAI/Azure scripts, ensure your `.env` file is configured with your endpoint, deployment, and API key.
- For the tokenization and vector DB demos, no API key is needed.

## What You'll Learn
- How LLMs can hallucinate (make up facts)
- How text is split into tokens
- How to get and compare vector embeddings
- How LLMs use attention to resolve ambiguity
- How to guide models with few-shot examples
- How to ground answers in private data (RAG)
- How to use a vector database for semantic search

---

Explore, experiment, and have fun learning the building blocks of modern AI systems!
