import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Roast Me 😂", page_icon="🔥")


st.markdown("""
<style>
body {
    overflow: hidden;
}

.particle {
    position: fixed;
    width: 6px;
    height: 6px;
    background: white;
    border-radius: 50%;
    opacity: 0.3;
    animation: float 10s infinite;
}

@keyframes float {
    0% { transform: translateY(100vh); }
    100% { transform: translateY(-10vh); }
}
</style>

<div class="particle" style="left:10%; animation-duration: 12s;"></div>
<div class="particle" style="left:30%; animation-duration: 15s;"></div>
<div class="particle" style="left:50%; animation-duration: 10s;"></div>
<div class="particle" style="left:70%; animation-duration: 18s;"></div>
<div class="particle" style="left:90%; animation-duration: 14s;"></div>
""", unsafe_allow_html=True)


# ---------------- API KEY ----------------
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3-flash-preview")

# ---------------- UI ----------------
st.title("🔥 Roast Me (but keep it fun 😭)")
st.write("Drop something about yourself... I'll roast you.")

user_input = st.text_area("Tell me about yourself:")

tone = st.selectbox(
    "Select roast level:",
    ["Mild 😌", "Savage 😈", "Unhinged 💀"]
)

# ---------------- PROMPT ----------------
def build_prompt(text, tone):
    return f"""
    You are a witty comedian. Roast the user in a funny, clever way.

    Rules:
    - No hate speech, no offensive content
    - Keep it humorous, not harmful
    - Make it sound like a stand-up comedy roast

    Roast Level: {tone}

    User description:
    {text}
    """

# ---------------- GENERATE ----------------
if st.button("Roast Me 🔥"):
    if user_input.strip() == "":
        st.warning("At least give me something to roast 😭")
    else:
        with st.spinner("Cooking your roast... 🍳"):
            prompt = build_prompt(user_input, tone)

            response = model.generate_content(prompt)

            st.subheader("💀 Your Roast:")
            st.write(response.text)