
def check_answer(question_text, user_answer):
    from openai import OpenAI

    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key="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")  # Replace with your actual API key

    # Prompt construction

    setup_prompt =  "Receive a question and a user response from Year 7-9 NSW quiz questions. Determine if the answer is correct, allowing for varied wording or spelling errors, and ignore units and spacing in math. Focus on content accuracy, especially in math, double-checking equations to avoid past mistakes. Return a Python string: '0' if correct, or '1|feedback' if incorrect, where feedback is max 2 concise sentences addressing the user as 'you' or 'your response,' providing insight into the correct answer before stating it."
    question = question_text
    user_answer = user_answer

    full_prompt = f"{setup_prompt}, the question is {question}, and the user response is {user_answer}"

    # Send a text-based question
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Use the appropriate model
        messages=[
            {"role": "user", "content": f"{full_prompt}"},
        ])

    # Capture the response in a variable
    answer = response.choices[0].message.content

    # Print the response
    return answer
