import openai

def generate_answer(api_key, query, retrieved_docs):
    client = openai.OpenAI(api_key=api_key)  # ✅ Set API key dynamically

    context = "\n".join(retrieved_docs)
    prompt = f"Use the following information to answer the question:\n\n{context}\n\nQuestion: {query}\nAnswer:"

    response = client.chat.completions.create(
        model="gpt-4",  # Or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
