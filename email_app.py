import streamlit as st

st.title("AI Email Reply Generator")

email_text = st.text_area("Enter Email Message")

def generate_reply(text):
    if not text:
        return "Please enter an email."

    if "interview" in text.lower():
        return "Thank you for the opportunity. I am available and look forward to the interview."

    if "meeting" in text.lower():
        return "Thank you for the update. I am available for the meeting and will join as scheduled."

    if "delay" in text.lower():
        return "Thank you for your patience. I apologize for the delay and will address it as soon as possible."

    return "Thank you for your email. I will review and get back to you shortly."

if st.button("Generate Reply"):
    reply = generate_reply(email_text)
    st.subheader("Suggested Reply:")
    st.write(reply)
    