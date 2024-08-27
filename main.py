# Initialized python file and installed all necessary langchain libraries

# Make sure you have downloaded Ollama in your system

#Then create a venv and install all the required modules using `pip install langchain langchain-ollama ollama`

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Passing multi-line string as a template for describing the instructions
template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer: 
"""

# Can replace the model name with other models
model = OllamaLLM(model="llama3")

prompt = ChatPromptTemplate.from_template(template)

# Creating a chain of both prompt and model
chain = prompt | model

def conversation():
    context = ""
    print("Welcone to the Python-Ollama AI Chatbot! Type `exit` to quit.")
    # Infinite loop for carrying on a conversation
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        
        res = chain.invoke({"context": "", "question": "hey how are you?"})
        print("AI: " + res)

        # Storing conversation history (Passing back the conversation)
        context += f"\nUser: {user_input}\nAI: {res}"

# Directly executing the Python file
if __name__ == "__main__":
    conversation()

