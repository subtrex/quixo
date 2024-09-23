# Quixo

## Resume Analysis using GPT-3.5 LLM

### Pipeline

This project is an interactive resume-based interview preparation tool that leverages the power of Large Language Models (LLM) to provide personalized and context-aware responses. Utilizing OpenAI's GPT-3.5-turbo as the core LLM, the system allows users to upload their resume, which is then parsed and embedded into a vector database using Chroma. Langchain's markdown parsing capabilities ensure the resume's sections are accurately segmented and indexed for efficient retrieval. When users engage with the chatbot, it employs a Conversational Retrieval Chain, which fetches relevant sections from the resume, providing tailored responses to interview questions.

Here are the main parts of the project along with the technologies used:

1. **Frontend Development**: 
   - **Technology**: Streamlit
   - **Purpose**: Created an interactive and user-friendly interface for users to interact with their resume-based chatbot.

2. **LLM Integration**:
   - **Technology**: OpenAI's GPT-3.5-turbo
   - **Purpose**: Powered the conversational retrieval chatbot to answer questions and simulate interview interactions based on the uploaded resume.

3. **Document Embedding**:
   - **Technology**: OpenAI Embeddings
   - **Purpose**: Converted the resume data into vector representations for efficient searching and retrieval.

4. **Vector Database**:
   - **Technology**: Chroma
   - **Purpose**: Stored and retrieved the vectorized resume data for quick access to relevant sections during conversations.

5. **Markdown Parsing**:
   - **Technology**: Langchain
   - **Purpose**: Processed the markdown-formatted resume to structure the content for further embedding and searching.

6. **Text Splitting & Chunking**:
   - **Technology**: RecursiveCharacterTextSplitter (Langchain)
   - **Purpose**: Split the resume content into manageable sections for more efficient querying and retrieval.

7. **Conversational Retrieval Chain**:
   - **Technology**: Langchain
   - **Purpose**: Enabled the integration of LLM responses with relevant resume context, ensuring accurate and context-aware interactions.
