import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

@st.cache_resource
def load_model():
    llm = HuggingFacePipeline.from_model_id(
        model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        task="text-generation",
        pipeline_kwargs={
            "max_new_tokens": 512,
            "do_sample": False,
            "repetition_penalty": 1.03,
        }
    )

    return ChatHuggingFace(llm=llm)

chat_model = load_model()

st.title("Local TinyLlama Chatbot")

query = st.text_input("Ask something")

if st.button("Submit") and query:
    response = chat_model.invoke(query)

    answer = response.content

    if "<|assistant|>" in answer:
        answer = answer.split("<|assistant|>")[-1].strip()

    st.write(answer)
