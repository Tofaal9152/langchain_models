from transformers import pipeline

# Load free public model
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-125M")

# Test prompt
prompt = "What is the capital of France?"
result = generator(prompt, max_length=50)

print(result[0]['generated_text'])
