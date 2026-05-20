from groq import Groq

client = Groq(
    api_key="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"
)

def generate_ai_response(user_query, recommendations):

    prompt = f"""
    User Query:
    {user_query}

    Recommended Products:
    {recommendations}

    Explain why these products are suitable.
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content