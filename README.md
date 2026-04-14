# False Explainer 🤥😭

A fun AI app that explains anything you type, but always lies.

## What it does
Enter any text, pick a lying style, and get a completely fabricated explanation delivered with full confidence.

## Lying Styles
Conspiracy theory, Science gibberish, Logical explanation, Like a dumb genius, Overconfident professor, GenZ, Millennial, Gen Alpha, Funny, Sarcastic, Sugar-coating, Custom and etc.

## Tech Stack
- Streamlit — frontend
- Groq API (llama-3.1-8b-instant) — LLM (model)
- OpenAI Python client — API calls
- python-dotenv — environment variables

## What I learned building this
- How to make API calls to an LLM
- Prompt engineering (system vs user roles)
- Real streaming responses with `stream=True` and how to manually stream responses using manual generator functions
- Streamlit basics — session state, spinner, selectbox
- Deploying a web app
- Securing the website so API abuse is avoided
- Git and Github basics very strongly

## Run locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Add a `.env` file with your `GROQ_API_KEY` and `APP_PASSWORD`
4. Run: `streamlit run app.py`
