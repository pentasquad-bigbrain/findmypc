import streamlit as st
import openai
import pandas as pd

st.set_page_config(page_title="AI PC Builder", layout="centered")
st.title("💻 AI PC Builder")
st.caption("Get personalized PC component recommendations with affiliate links!")

# --- OpenAI API ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

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
        # Prepare AI prompt
        prompt = f"""
        Suggest a complete PC build for the following:
        Use case: {use_case}
        """
        if gaming_type:
            prompt += f" Gaming types: {', '.join(gaming_type)}"
        prompt += f" Budget: ${budget}.\nProvide a table of recommended components (CPU, GPU, RAM, Motherboard, Storage, PSU, Case), prices, compatibility check, and short affiliate link placeholders."

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful PC building assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=800
            )
            result = response["choices"][0]["message"]["content"]

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

        except Exception as e:
            st.error(f"⚠️ Error generating build: {e}")

# --- Step 5: Budget warning ---
st.info("💡 Tip: You can adjust your budget to get better component suggestions.")
