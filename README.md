# findmypc

# Smart Product Comparison Tool (Streamlit + OpenAI)

Compare two products side-by-side (features, pros/cons, use cases) and attach affiliate links.

## 🚀 Quickstart (Local)

1. **Clone or create a folder** and put `app.py` inside it.
2. Create a virtual environment:
   - Windows: `python -m venv .venv && .venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv .venv && source .venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Add your OpenAI key to `.streamlit/secrets.toml`:
   ```toml
   OPENAI_API_KEY = "sk-your-key"
   ```
5. Run the app: `streamlit run app.py`

## ☁️ Deploy on Streamlit Community Cloud

1. Push `app.py` and `requirements.txt` to GitHub (public or private repo).
2. Create a new app on Streamlit Community Cloud and select your repo/branch.
3. In **App settings → Secrets**, add:
   ```
   OPENAI_API_KEY="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"
   ```
4. Deploy.

## 🔧 Notes
- This app uses `openai==0.28.x` (ChatCompletion). If you prefer the new SDK,
  update the code to use `from openai import OpenAI` and `client.chat.completions.create(...)`,
  or pin `openai==0.28.1` as provided.
- Replace the placeholder affiliate URLs with your actual tagged links.
