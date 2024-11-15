---

# AI Poem Crafter ✨📝

**AI Poem Crafter** is a creative web app that generates beautiful poems using the **AwanLLM API**! 🎤🎶 Whether you're in the mood for a happy, sad, or nostalgic poem, this app allows you to customize the mood, length, and even theme to create a unique piece of art. 🌟

### Key Features 🌟
- **Generate Poems**: Select a mood, length, and theme (optional) to generate a personalized poem. 🖋️
- **Poem History**: Keep track of all your generated poems with titles, moods, and content. 📜
- **Download Poems**: Download your poems as text files with the title as the filename. 💾
- **Copy to Clipboard**: Easily copy any poem to your clipboard for sharing. 📋
- **Clear History**: Reset your poem history with a single click. 🧹

---

## How to Use 💡

1. **Choose Your Poem Settings**: 
   - Select a **mood** (e.g., Happy, Sad, Romantic, etc.)
   - Choose your **poem length** (Short, Medium, or Long).
   - Optionally, enter a **theme** or keywords.
   
2. **Generate Your Poem**: 📝 
   - Click the **"Generate Poem"** button, and wait as the AI crafts your masterpiece! ✨
   
3. **Poem History**: 🏛️
   - View all the poems you've created, with the option to expand them for full reading.
   
4. **Download or Copy**: 🔽
   - **Download** poems as `.txt` files, or **copy** them directly to your clipboard for easy sharing.

5. **Clear History**: 🧹
   - Use the **Clear Poem History** button to reset all your poem data.

---

## Requirements 📦

- Python 3.7+ 🐍
- **Streamlit** 📊
- **Requests** 🔌
- **Pyperclip** 📋

---

## Installation ⚙️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/eternalflame02/AI-Poem-Crafter.git
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally**:
   ```bash
   streamlit run poemcrafter.py
   ```

---

## Deploy to Streamlit Cloud ☁️

1. Sign in to your **Streamlit** account [here](https://streamlit.io).
2. Go to your dashboard and click **"New app"**.
3. Connect your **GitHub repository** and deploy the app.
4. **Set your API_KEY** as a secret in Streamlit Cloud:
   - In **Streamlit Cloud**, navigate to **Settings** > **Secrets** and add your **API_KEY**.
   - Example:
     ```toml
     [secrets]
     API_KEY = "your-api-key-here"
     ```

---

## Contributing 🤝

I welcome contributions! Feel free to fork the repo, create branches, and submit pull requests. 

---

## License 📜

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details. 📄

---

Thanks for checking out **AI Poem Crafter**
---
