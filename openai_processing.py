import openai

# Replace 'your-api-key' with your actual OpenAI API key
api_key = ''

# Set up the OpenAI API client
openai.api_key = api_key

def generate_bot_response(comment):
    # Create the GPT-3.5 Turbo response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Draft a brief reply of upto 20 tokens to the following YouTube video comment: '{comment}'"}
        ],
        max_tokens=40  # You can adjust this value based on your desired response length
    )

    # Extract and return the response
    bot_response = response.choices[0].message['content']
    return bot_response

