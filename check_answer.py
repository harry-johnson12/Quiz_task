
def check_answer(question_text, user_answer):
    from openai import OpenAI
    # Initialize the OpenAI client with your API key
    key=""
    client = OpenAI(api_key=key)  # Key stopped working again so just put one here that works (I checked it was definitely the key)

    # Prompt construction
    setup_prompt =  "You will receive a question and a user response from Year 7-9 NSW quiz questions. Determine if the answer is correct, allowing for varied wording or spelling errors, and ignore units and spacing in math. Focus on accuracy and reason in checking mathematical answers. Return a string: '0' if correct, or '1|feedback' if incorrect, where feedback is max 2 concise sentences, dont start with 'feedback' address the user as 'you' or 'your response,' providing insight into the correct answer before linking back to it. Avoid contradicting yourself in feedback by saying your response 'x' was incorrect the correct answer was 'x'."
    question = question_text
    user_answer = user_answer

    full_prompt = f"{setup_prompt} The question is {question}, and the user response is {user_answer}"

     # Send a text-based question
    response = client.chat.completions.create(
    model="gpt-4o",  # Using 4o for accuracy instead of 3.5 - this might be costing you a lot more but you tell me
        messages=[
            {"role": "user", "content": f"{full_prompt}"},
        ])

    # Capture the response in a variable
    answer = response.choices[0].message.content

    # Print the response
    return answer
