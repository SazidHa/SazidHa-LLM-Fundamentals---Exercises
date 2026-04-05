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
## Hallucianate
<img width="781" height="377" alt="image" src="https://github.com/user-attachments/assets/80672fd8-187a-42da-8466-4442c938eda2" />

## Tokenization
What is Tokenization?
Tokenization is the process of splitting text into smaller units called tokens, which could be:

Words: "Artificial intelligence is amazing!" → ["Artificial", "intelligence", "is", "amazing", "!"].
Subwords: For example, "unbelievable" → ["un", "believable"].
Characters: In some cases, each letter can be treated as a token (e.g., "AI" → ["A", "I"]).

Once tokens are created, they are converted into unique numerical IDs that the model can process. 
How Are Tokens Assigned Numbers?
Each token is mapped to a unique number based on the model’s vocabulary file, which is essentially a lookup table of all possible tokens the model knows.

<img width="317" height="173" alt="image" src="https://github.com/user-attachments/assets/aa1baccd-c657-47c7-b2eb-628bc9cf2257" />
<img width="317" height="173" alt="Tokenizatrion" src="https://github.com/user-attachments/assets/453032a3-5c5c-4c2e-92c1-2863d3072f20" />

## Vectorization
What is Vectorization?
Vectorization is the process of representing qualitative information (e.g., text or categories) as quantitative data (e.g., vectors or matrices). This transformation makes it possible for computational models to analyze and interpret the information.

<img width="308" height="244" alt="image" src="https://github.com/user-attachments/assets/3d2562a0-dbe0-468c-98ed-6f0f28e5e1db" />
<img width="308" height="244" alt="Vectorization_example" src="https://github.com/user-attachments/assets/92a25442-b82d-4428-8c23-d186329e92c3" />

## Attention
What is attention mechanism?
The attention mechanism in Large Language Models (LLMs) allows models to dynamically focus on relevant parts of an input sequence, assigning weights to words based on context rather than treating them independently. 
Explore, experiment, and have fun learning the building blocks of modern AI systems!

<img width="250" height="157" alt="image" src="https://github.com/user-attachments/assets/a39e5812-57b0-4aee-879c-0e6db3c2b869" />
<img width="291" height="139" alt="attention_example" src="https://github.com/user-attachments/assets/63481f4c-f396-48f9-b0ba-edb04d1a16c3" />

## Few-Shot Prompting
What is few shot promting?
Few-shot prompting is a technique that provides an AI model with a few examples (or "shots") of input-output pairs within the prompt to guide its response to a new task.

<img width="263" height="110" alt="image" src="https://github.com/user-attachments/assets/9cb60449-9e4b-4836-935b-ba75d2e7f67a" />
<img width="263" height="110" alt="Few_shot" src="https://github.com/user-attachments/assets/aae17bfb-f32a-4fb8-adec-5b94e9de7249" />

## Retrieval-Augmented Generation (RAG)
Retrieval augmented generation, or RAG, is an architecture for optimizing the performance of an artificial intelligence (AI) model by connecting it with external knowledge bases. RAG helps large language models (LLMs) deliver more relevant responses at a higher quality.

<img width="238" height="44" alt="rag_exaple" src="https://github.com/user-attachments/assets/b5c3d796-0bd9-4be1-bd9b-38310c737160" />

## Vector Database Search
Vector database search (or vector search) is a method for finding similar items by comparing high-dimensional vectors (embeddings) representing data meaning rather than exact keywords. It uses AI models to convert unstructured data—text, images, audio—into semantic vectors, using algorithms like HNSW to instantly identify "nearest neighbor" matches.

<img width="229" height="182" alt="image" src="https://github.com/user-attachments/assets/2e3adf55-1a1b-4a4b-8453-3df160454701" />
<img width="229" height="180" alt="vector_db_example" src="https://github.com/user-attachments/assets/2f1bca56-12f8-47f1-97e4-1841e85d35d5" />

