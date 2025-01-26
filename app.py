import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_chroma import Chroma
from models import Models
import asyncio
import time

# Initialize the models
models = Models()
embeddings = models.embeddings_ollama
llm = models.model_ollama

# Initialize the vector store
vector_store = Chroma(
    collection_name="documents",
    embedding_function=embeddings,
    persist_directory="./db/chroma_langchain_db",  # Ensure this matches the volume mount path in docker-compose.yml
)

# Define the chat prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant speaking only in Polish language. You read feelings and suggest a song to improve your mood. Answer the question based only on the data provided."),
        ("human", "Use the user question {input} to answer the question. Use only the {context} to answer the question.")
    ]
)

# Define the retrieval chain
retriever = vector_store.as_retriever(kwargs={"k": 5})
combine_docs_chain = create_stuff_documents_chain(
    llm, prompt
)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

# Streamlit app
st.title("Song Recommendation Chat")

# Chat interface
st.write("Tell me about your mood or what kind of song you're looking for:")
user_input = st.text_input("You:")

# Placeholder for the response
response_placeholder = st.empty()

if user_input:
    try:
        # Debugging: Print the user input
        print(f"User input: {user_input}")

        # Measure the start time
        start_time = time.time()

        # Asynchronous processing
        async def process_request():
            result = await retrieval_chain.ainvoke({"input": user_input})
            return result

        # Run the asynchronous processing
        result = asyncio.run(process_request())

        # Measure the end time
        end_time = time.time()

        # Calculate the response time
        response_time = end_time - start_time
        print(f"response_time: {response_time}")

        # Debugging: Print the result
        print(f"Result: {result}")

        # Ensure the result contains the expected keys
        if "answer" in result:
            response_placeholder.markdown(f"Assistant: {result['answer']}")
            st.write(f"Response time: {response_time:.2f} seconds")
        else:
            response_placeholder.text("Assistant: No response generated.")
    except Exception as e:
        response_placeholder.error(f"Error: {e}")
