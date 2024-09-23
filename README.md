# Quixo

## Resume Analysis using GPT-3.5 LLM

### Pipeline

This project is an interactive resume-based interview preparation tool that leverages the power of Large Language Models (LLM) to provide personalized and context-aware responses. Utilizing OpenAI's GPT-3.5-turbo as the core LLM, the system allows users to upload their resume, which is then parsed and embedded into a vector database using Chroma. Langchain's markdown parsing capabilities ensure the resume's sections are accurately segmented and indexed for efficient retrieval. When users engage with the chatbot, it employs a Conversational Retrieval Chain, which fetches relevant sections from the resume, providing tailored responses to interview questions.
