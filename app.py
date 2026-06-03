import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

st.set_page_config(
    page_title="TinyLlama Chatbot",
    page_icon="🤖",
    layout="wide"
)

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

st.title("🤖 TinyLlama Chatbot")
st.caption("Local AI Assistant powered by TinyLlama")

query = st.text_area(
    "Ask your question",
    height=120,
    placeholder="Type your question here..."
)

if st.button("🚀 Generate Response", use_container_width=True):
    if query:
        with st.spinner("Thinking..."):
            response = chat_model.invoke(query)

            answer = response.content

            if "<|assistant|>" in answer:
                answer = answer.split("<|assistant|>")[-1].strip()

        st.success("Response Generated")

        st.markdown("### Answer")
        st.info(answer)
