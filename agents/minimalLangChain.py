from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
import os

# load your OpenAI key (export OPENAI_API_KEY first in terminal)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, openai_api_key=OPENAI_API_KEY)
chat = ConversationChain(llm=llm, verbose=True)

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    response = chat.run(user_input)
    print("Bot:", response)



