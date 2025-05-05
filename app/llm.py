import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def ask_llm(question:str) -> str:
    with open("llm_context.txt", "r") as f:
        context = f.read()                 



      
    llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            )
    prompt_template = """
    You are a helpful assistant for an API server. Based on the provided context, answer user questions clearly and accurately. 
    If you don't know the answer, respond with 'Sorry! I'm not sure about that.
    Given quesrtion:
    {question}
    Given context: 
    {context}"""
    
    

    prompt = prompt_template.format(
                
                context=context,
                question=question,
            )
            
    response = llm.invoke(prompt)
    return response.content

    
'''question = "What is the purpose of this API?" 
response = ask_llm(question)
print(response)'''