import streamlit as st
import requests
import pyperclip

# AwanLLM API Configuration
API_URL = "https://api.awanllm.com/v1/completions"  
API_KEY = st.secrets["API_KEY"] 

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# App-wide variables
if "poem_history" not in st.session_state:
    st.session_state.poem_history = []

def generate_poem(mood, length, theme=None):
    """Generate a poem using the AwanLLM API."""
    prompt = f"Write a {length.lower()} {mood.lower()} poem"
    if theme:  # Only adds the theme if it's provided
        prompt += f" about {theme}."
    
    payload = {
        "model": "Meta-Llama-3.1-70B-Instruct",
        "prompt": prompt,
        "max_tokens": 150 if length == "Short" else 300 if length == "Medium" else 500,
        "temperature": 0.7
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        generated_text = response.json().get("choices", [{}])[0].get("text", "")
        return generated_text.strip()
    else:
        return f"Error: {response.status_code} - {response.text}"


def copy_to_clipboard(poem):
    """Copy poem to clipboard using pyperclip."""
    pyperclip.copy(poem)
    st.success("Poem copied to clipboard!")

def download_poem(poem, title, key):
    """Download poem as a text file with a unique key and include the title in the file name."""
    file_name = f"{title}.txt"  # Uses poem title as the file name
    st.download_button(
        label="Download Poem as Text",
        data=poem,
        file_name=file_name,
        mime="text/plain",
        key=key
    )

# Streamlit Page Config
st.set_page_config(page_title="AI Poem Crafter", page_icon="✍️", layout="wide")

st.title("✨ AI Poem Crafter")

# Layout: Mood Selection, Poem Length, and Theme
with st.sidebar:
    st.header("📜 Choose Poem Settings")
    mood = st.selectbox("Select Your Mood:", ["Happy", "Sad", "Nostalgic", "Hopeful", "Adventurous", "Excited", "Melancholic", "Romantic", "Calm"])
    length = st.selectbox("Select Poem Length:", ["Short", "Medium", "Long"])
    theme = st.text_input("Enter a Theme or Keywords (Optional):")

# Main Interface
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 Your Poem")
    
    # Poem Length Display
    st.write(f"**Poem Length Selected:** {length}")
    
    # Generate Poem Button
    if st.button("Generate Poem"):
        with st.spinner("Crafting your poem..."):
            poem = generate_poem(mood, length, theme)
            if poem:
                title = poem.splitlines()[0] if len(poem.splitlines()) > 0 else "Untitled Poem"
                st.session_state.poem_history.append({"title": title, "mood": mood, "content": poem})
                st.text_area("Generated Poem:", poem, height=300)
                
                download_poem(poem, title, key="main_poem_download")  # Poem title 
            else:
                st.error("No poem was generated.")
                
    # Clear Button to reset poem history
    if st.button("Clear Poem History"):
        st.session_state.poem_history = []
        st.info("Poem history has been cleared.")

with col2:
    st.subheader("📜 Poem History")
    if st.session_state.poem_history:
        for i, poem_data in enumerate(st.session_state.poem_history[::-1], start=1):
            with st.expander(f"{poem_data['mood']} - {poem_data['title']}"):
                st.write(poem_data["content"])
                
                # Copy button for each poem in history
                if st.button(f"Copy to Clipboard ({poem_data['title']})", key=f"copy_{i}"):
                    copy_to_clipboard(poem_data["content"])  # Copy the specific poem
                download_poem(poem_data["content"], poem_data["title"], key=f"download_{i}")  # Poem title 
    else:
        st.info("No poems in history yet.")

# Footer 
st.markdown(
    """
    <hr>
    <footer style="text-align: center;">
        Made with ❤️ and AI by You. Keep writing and dreaming!
    </footer>
    """,
    unsafe_allow_html=True
)
