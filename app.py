import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="AI PC Builder", layout="centered")
st.title("💻 AI PC Builder (Hugging Face Edition)")

# --- Hugging Face API ---
HF_API_KEY = st.secrets["HF_API_KEY"]
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query_hf(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        return f"⚠️ Error: {response.text}"

# --- Step 1: Ask user for use case ---
use_case = st.selectbox(
    "What will you mainly use your PC for?",
    ["Gaming", "Office / Productivity", "Content Creation / Video Editing", "Programming / Development"]
)

# --- Step 2: Gaming specifics if chosen ---
gaming_type = None
if use_case == "Gaming":
    gaming_type = st.multiselect(
        "Select the types of games you play",
        ["Esports / Competitive", "AAA Games", "Indie / Casual"]
    )

# --- Step 3: Budget ---
budget = st.number_input("Enter your budget (in USD)", min_value=200, step=50)

# --- Step 4: Generate PC recommendation ---
if st.button("Generate Build"):
    with st.spinner("Generating your PC build..."):
        prompt = f"Suggest a complete PC build for {use_case}, budget ${budget}."
        if gaming_type:
            prompt += f" Gaming types: {', '.join(gaming_type)}."
        prompt += " Provide a list of CPU, GPU, RAM, Motherboard, Storage, PSU, Case with compatibility notes."

        result = query_hf(prompt)

        st.markdown("### 🖥 Recommended PC Build")
        st.markdown(result)

        # Example affiliate links (replace with your links)
        st.markdown("### 🛒 Affiliate Links")
        st.markdown("- CPU: [Buy Here](https://amzn.to/example1)")
        st.markdown("- GPU: [Buy Here](https://amzn.to/example2)")
        st.markdown("- RAM: [Buy Here](https://amzn.to/example3)")
        st.markdown("- Motherboard: [Buy Here](https://amzn.to/example4)")
        st.markdown("- Storage: [Buy Here](https://amzn.to/example5)")
        st.markdown("- PSU: [Buy Here](https://amzn.to/example6)")
        st.markdown("- Case: [Buy Here](https://amzn.to/example7)")

st.info("💡 Tip: You can adjust your budget to get better component suggestions.")
