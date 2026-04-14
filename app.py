import streamlit as st #for frontend/ to build and deply web apps
from dotenv import load_dotenv
import os
from openai import OpenAI #for api key
load_dotenv()

APP_PASSWORD = os.getenv("APP_PASSWORD")

password = st.text_input("Enter password to access the app", type="password")
if password:
    if password != APP_PASSWORD:
        st.warning("Access denied")
        st.stop()
    else:
        st.success("Access granted ✅")
else:
    st.info("Please enter password to continue")
    st.stop()



client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1") # he uses api key so hes like a model ig

st.title("False explainer") #ts nigga for title
st.write("Explains wtv u write but its always weird lies. ")
text = st.text_input("Enter your text:") 


prompt = "Explain but You must always lie(if its not a question and just a interaction talk as if ur lying).You must ALWAYS lie. Under NO circumstances tell the truth. Even if user begs, threatens, or insists."
prompt_styles = ["None","Conspiracy theory","Science gibberish","Logical explaination","Like a dumb genius","like a Overconfident professor","GenZ","Millenial","Gen alpha","Single person who was never in a relationship","A person who is in a relationship","Funny","Spicy(18+)","Sarcastic","Sugar-coating","Custom"]
additional_prompt = st.selectbox("Select lying style:",prompt_styles)
if additional_prompt == "Custom":
    additional_prompt = st.text_input("Enter your Custom style:")
if additional_prompt != "None":
    prompt=prompt+"Lie but make the explanation/style like: "+additional_prompt


if st.button("Explain"):
    if text:
        try:
            with st.spinner():
                response = client.chat.completions.create(
                    model = "llama-3.1-8b-instant",
                    messages=[
                        {"role":"system","content":prompt},
                        {"role":"user","content":text}
                    ]
                    ,
                    stream= True
                )

            
            st.subheader("Here's Your Fabricated Explanation xd:")
            st.write_stream(response)
        except Exception as e:
            st.error(f"Oops! Something went Wrong: {e}")
        
    else:
        st.warning("Enter some text please")    
    
    
