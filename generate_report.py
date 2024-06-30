from transformers import pipeline

# Load pre-trained GPT-4 model (using a placeholder model)
nlp = pipeline('text-generation', model='gpt-4')

# Sample audit data
audit_data = "Detected multiple transactions with anomalies..."

# Generate report
report = nlp(f"Generate a detailed audit report based on the following data: {audit_data}", max_length=512)[0]['generated_text']

print(report)