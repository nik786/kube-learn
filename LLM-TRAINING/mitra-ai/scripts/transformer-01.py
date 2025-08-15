from transformers import pipeline
import torch

# Optional: speed up CPU inference
torch.set_num_threads(4)  # adjust based on your CPU cores

# Force CPU (-1) and use a smaller model
roberta = pipeline(
    "zero-shot-classification",
    model="typeform/distilbert-base-uncased-mnli",
    device=-1
)

sequence1 = "My son is sick and needs to be hospitalized"
labels1 = ['health insurance', 'auto insurance', 'property damage', 'accident claim', 'others']
print(roberta(sequence1, labels1))

sequence2 = "Sky is blue and Sun is hot"
labels2 = ['sensitive info', 'public info']
print(roberta(sequence2, labels2))

