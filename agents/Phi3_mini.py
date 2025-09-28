from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from langchain_community.llms import HuggingFacePipeline
import torch

# 1. Load tokenizer & model (Phi-3-mini)
model_name = "microsoft/Phi-3-mini-4k-instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    device_map="auto",
    torch_dtype=torch.float16,
    trust_remote_code=True
)

# Set pad token if not exists
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

# 2. Create text-generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=200,
    temperature=0.7,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id,
    return_full_text=False  # Only return new generated text
)

# 3. Wrap it in LangChain
llm = HuggingFacePipeline(pipeline=pipe)

print("🤙 SurfSense is ready! Type 'quit' to exit.")

# 4. Conversation loop with proper formatting
chat_template = "<|user|>\n{user_input}<|end|>\n<|assistant|>\n"

while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit"]:
        break
    
    # Format input for Phi-3
    formatted_input = chat_template.format(user_input=user_input)
    
    try:
        response = llm.invoke(formatted_input)
        print("Bot:", response.strip())
    except Exception as e:
        print(f"Error: {e}")
        break