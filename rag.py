from llama_cpp import Llama

llm = Llama.from_pretrained(
	repo_id="brittlewis12/Meta-Llama-3.1-8B-Instruct-GGUF",
	filename="meta-llama-3.1-8b-instruct.IQ1_M.gguf",
)
response = llm.create_chat_completion(
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(response['choices'][0]['message']['content'])