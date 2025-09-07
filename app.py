
import streamlit as st
import openai

st.set_page_config(page_title="Smart Product Comparison Tool", layout="centered")

st.title("🔍 Smart Product Comparison Tool")
st.write("Compare two products side by side before you buy. All links are affiliate supported.")

# --- OpenAI API setup ---
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Inputs ---
prod1 = st.text_input("Enter Product 1 Name or Link:")
prod2 = st.text_input("Enter Product 2 Name or Link:")

if st.button("Compare"):
    if prod1 and prod2:
        with st.spinner("Analyzing products..."):
            prompt = f"""Compare these two products in detail: {prod1} vs {prod2}.
            Provide a table with key features, pros, cons, and best use cases.
            """
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "system", "content": "You are a product comparison assistant."},
                          {"role": "user", "content": prompt}],
                max_tokens=600
            )
            comparison = response["choices"][0]["message"]["content"]
            st.markdown("### 📊 Comparison Result")
            st.markdown(comparison)

            # Affiliate links placeholder (replace with real links)
            st.markdown("### 🛒 Buy Links")
            st.markdown(f"- [Buy {prod1} (Affiliate Link)](https://amzn.to/example1)")
            st.markdown(f"- [Buy {prod2} (Affiliate Link)](https://amzn.to/example2)")
    else:
        st.error("Please enter both product names or links to compare.")
