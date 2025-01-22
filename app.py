import streamlit as st
import pickle

# Title of the app
st.title("Question Answering System")
st.write("Ask a question, and the system will provide an answer based on the indexed documents.")

# Load the saved QA chain
@st.cache_resource
def load_qa_chain():
    with open("./data/model/qa_chain.pkl", "rb") as f:
        return pickle.load(f)

qa_chain = load_qa_chain()

# Input field for user question
query = st.text_input("Enter your question:")

# Process the query and display the result
if query:
    with st.spinner("Retrieving and generating an answer..."):
        response = qa_chain.invoke({"query": query})
        answer = response["result"]

        # Clean and format the answer
        clean_answer = (
            answer.replace("/quotesingle.ts1", "'")
                  .replace(": ", ":\n\t")
                  .replace(") ", ")\n\t")
                  .strip()
        )

        # Display the formatted answer
        st.subheader("Answer:")
        st.code(clean_answer, language="python")
