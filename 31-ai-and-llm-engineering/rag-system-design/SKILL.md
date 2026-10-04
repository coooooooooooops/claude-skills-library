---
name: rag-system-design
description: "Design retrieval-augmented generation: chunking, embeddings, vector stores, reranking, and evaluation. Use when grounding LLMs in your documents."
---

# Rag System Design

Design retrieval-augmented generation: chunking, embeddings, vector stores, reranking, and evaluation.

## Process

1. Define sources and questions
2. chunk with overlap
3. embed and index
4. retrieve and rerank
5. cite sources in answers
6. evaluate retrieval

## Output format

RAG architecture and code.

## Rules

- Evaluate retrieval separately from generation.
- Ask at most one or two clarifying questions when key inputs are missing; otherwise state assumptions and proceed.
- Match the user's level and tone; keep the response as short as the task allows.
