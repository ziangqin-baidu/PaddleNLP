from paddlenlp.transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("linly-ai/chinese-llama-2-7b", dtype="float16")

print("> finished!")
