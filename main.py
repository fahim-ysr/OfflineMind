# Initialized python file and installed all necessary langchain libraries

# Make sure you have downloaded Ollama in your system

#Then create a venv and install all the required modules using `pip install langchain langchain-ollama ollama`

from langchain_ollama import OllamaLLM

# Can replace the model name with other models
model = OllamaLLM(model="llama3")

res = model.invoke(input= "Hello, what are you?")
print(res)