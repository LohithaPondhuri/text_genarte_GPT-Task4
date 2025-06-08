from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
import sys

# Load pre-trained GPT-2 model and tokenizer
model_name = "gpt2"

try:
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
except Exception as e:
    print(f"❌ Error loading model: {e}")
    sys.exit()

model.eval()

# Function to generate text from a prompt
def generate_text(prompt, max_length=150):
    if not prompt.strip():
        return "❌ Prompt is empty. Please provide a valid input."

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(
            inputs,
            max_length=max_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=1.0
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Example usage
if __name__ == "__main__":
    try:
        user_prompt = input("Enter your prompt: ")
        print("\n📝 Generated Text:\n")
        print(generate_text(user_prompt))
    except KeyboardInterrupt:
        print("\n❌ Process interrupted by user.")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
