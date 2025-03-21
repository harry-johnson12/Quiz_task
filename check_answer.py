
def check_answer(question_text, user_answer):
    from openai import OpenAI

    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key="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")  # Replace with your actual API key

    # Prompt construction

    setup_prompt =  "You will recieve a question and user response to that question. They are pretty basic general knowledge questions. I would like you to work out if they have the answer correct, if so, return a very simple Python string, that looks like this -- 0 if they are correct or 1|feedback if they are incorrect - the feedback should be max 2 sentences. Give some insight into the correct answer, dont just say thats wrong, this is the correct answser.)"
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
