# **DocChat: Chat with Your Documents**

DocChat is an advanced chatbot that allows you to interact with your documents PDF, TXT, DOCX etc in a natural and conversational manner. By leveraging the power of LangChain, Gemini, Ollama & Streamlit, DocChat delivers an intuitive and informative user experience.

---

## **Features**

- **Conversational Interaction:** Engage in natural conversations about your documents and receive detailed responses.
- **Multi-Document Support:** Upload and process a variety of document formats, including PDFs, text files, Word documents, spreadsheets, and presentations.
- **Website-Chat Integration:** Chat with any valid website by providing a URL.
- **Advanced Language Models:** Choose from state-of-the-art LLMs like Ollama, Groq, and Gemini for enhanced chatbot responses.
- **Embedding Models:** Use Ollama Embeddings or GooglePalm Embeddings to improve document understanding.
- **User-Friendly Interface:** A clean and simple interface powered by Streamlit for seamless interactions.

---

## **Installation**

### **Prerequisites**

- Python 3.10 or higher
- A virtual environment (recommended)

---

### **Clone the Repository**

Clone the DocChat repository from GitHub:

```bash
git clone https://github.com/pr0ximaCent/DocChat-LLM_Powered_Chatbot.git
```

---

### **Navigate to the Working Directory**

```bash
cd DocChat
```

---
### **Using Rye (Recommended)**

1. Install the Rye package manager: [Installation Guide](https://rye-up.com/guide/installation/).

2. Sync the project:

   ```bash
   rye sync
   ```

---

### **Using venv**

1. Create a virtual environment:

   ```bash
   python -m venv docchat-env
   ```

2. Activate the virtual environment:

   - On Linux/MacOS:
     ```bash
     source docchat-env/bin/activate
     ```
   - On Windows:
     ```bash
     docchat-env\\Scripts\\activate
     ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

### **Using Conda**

1. Create a Conda environment:

   ```bash
   conda create -n docchat-env python=3.12
   ```

2. Activate the Conda environment:

   ```bash
   conda activate docchat-env
   ```

3. Install the required dependencies:

   ```bash
   conda install --file requirements.txt
   ```

---

## **Configuration**

Rename the `secrets_example.toml` file to `secrets.toml` in the `src/docchat/.streamlit/` directory:

```bash
mv src/docchat/.streamlit/secrets_example.toml src/docchat/.streamlit/secrets.toml
```

---

## **Ollama Installation**

To use Ollama in DocChat, follow these steps:

1. **Install Ollama:**
   - Visit the official Ollama website for installation instructions: [Ollama Download](https://ollama.com/download).

2. **Download Ollama Models:**

   Open your terminal and run the following commands to download the necessary models:

   - Download the `nomic-embed-text` model (required for embeddings):
     ```bash
     ollama pull nomic-embed-text
     ```

   - Download the `openchat` model (for language model functionality):
     ```bash
     ollama pull openchat
     ```

---

## **Usage**

### **1. Set API Keys**

If you're using Google Gemini or Groq, obtain the necessary API keys and securely store them in the `src/docchat/.streamlit/secrets.toml` file or upload them through the chatbot interface.

---

### **2. Run the Application**

- **With Streamlit:**
  ```bash
  cd src/docchat
  streamlit run chatbot.py
  ```

- **Using Rye:**
  ```bash
  cd src/docchat
  rye run streamlit run chatbot.py
  ```

---

### **3. Upload Documents**

In the Streamlit interface:
- Upload the documents you want to chat with.
- Click the **"Process"** button to analyze the uploaded files.

---

### **4. Start Chatting**

Once the documents are processed:
- Enter your questions in the chat input field.
- The chatbot will analyze your documents and provide precise, contextual answers.

---

## **Additional Notes**

- For optimal performance, ensure your system has sufficient resources (CPU, RAM) for document processing and LLM computations.
- Use a GPU-enabled environment, if available, to accelerate processing and response time.
- The chatbot's performance may vary depending on the complexity and length of your documents.

---

