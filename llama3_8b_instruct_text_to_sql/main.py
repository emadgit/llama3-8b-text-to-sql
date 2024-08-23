import lamini
import os

lamini_api_key = os.getenv('POETRY_LAMINI_API_KEY') # Get your API KEY from https://app.lamini.ai/account

lamini.api_key = lamini_api_key

llm = lamini.Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")

def start():
    prompt = ( 
    "<|begin_of_text|>"  # Start of prompt
    "<|start_header_id|>system<|end_header_id|>\n\n"  #  header - system
    "You are a helpful assistant."  # system prompt
    "<|eot_id|>" # end of turn
    "<|start_header_id|>user<|end_header_id|>\n\n" # header - user
    "Please write a birthday card for my good friend Andrew" 
    "<|eot_id|>" # end of turn
    "<|start_header_id|>assistant<|end_header_id|>\n\n" # header - assistant
    )
    print(prompt)
    result = llm.generate(prompt, max_new_tokens=200)
    print(result)