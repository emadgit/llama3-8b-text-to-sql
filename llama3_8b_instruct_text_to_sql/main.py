import lamini
import os

lamini_api_key = os.getenv('POETRY_LAMINI_API_KEY') # Get your API KEY from https://app.lamini.ai/account

lamini.api_key = lamini_api_key

llm = lamini.Lamini(model_name="meta-llama/Meta-Llama-3-8B-Instruct")

def start():
    system_prompt = user_prompt = "You are a helpful assistant."
    user_prompt = "Please write a birthday card for my good friend Andrew"
    prompt = make_llama_3_prompt(user_prompt, system_prompt)
    print(prompt)
    result = llm.generate(prompt, max_new_tokens=200)
    print(result)


def make_llama_3_prompt(user, system=""):
    system_prompt = ""
    if system != "":
        system_prompt = (
            f"<|start_header_id|>system<|end_header_id|>\n\n{system}"  #  header - system prompt
            f"<|eot_id|>" # end of turn
        )
    prompt = (
        f"<|begin_of_text|>{system_prompt}" # Start of prompt
        f"<|start_header_id|>user<|end_header_id|>\n\n" # start header - user
        f"{user}"
        f"|eot_id|" # end of turn
        f"<|start_header_id|>assistant<|end_header|>\n\n" # header - assistant
    )
    return prompt