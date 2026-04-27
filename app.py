import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("AI Resume Analyzer")

resume_text = st.text_area("Paste Resume Text")

if st.button("Analyze"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Extract skills and summarize resume."},
            {"role": "user", "content": resume_text}
        ]
    )
    st.write(response.choices[0].message.content)