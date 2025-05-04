from transformers import AutoTokenizer, AutoModel
import torch

# Model ve tokenizer'ı yükle
model_name = "deepseek-ai/deepseek-embedding-v1-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def get_prompt_embedding(prompt):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1)  # Ortalama alınarak tek bir vektör elde edilir
    return embeddings[0]  # Tek vektör (boyut: 768)
