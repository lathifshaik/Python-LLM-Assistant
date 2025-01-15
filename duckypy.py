import ollama
import random
import time
import sys


def get_dynamic_greeting():
    """
    Generates a random exciting greeting for the user.
    :return: A programming-focused greeting string.
    """
    greetings = [
        "Hey there, Pythonista! Ready to debug or build something awesome? 🐍",
        "Hello, coder extraordinaire! Let's craft some elegant solutions. 💻",
        "Hi there! Let's bring your programming ideas to life. 🚀",
        "Welcome back, developer! What Python magic shall we weave today? 🧑‍💻",
        "Yo! Ready to write some beautiful code? 🌟",
        "Hola! Let’s dive into some programming adventures. 🪄✨"
    ]
    return random.choice(greetings)


def dynamic_typing_effect(text, delay=0.03):
    """
    Simulates a typing effect by displaying text character by character.
    :param text: The complete text to display.
    :param delay: Time delay between displaying each character.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Move to the next line


def generate_response(query, chat_history, model="llama3.2", retries=3):
    """
    Generates programming-focused responses, with memory management and retry logic.
    :param query: The user's input.
    :param chat_history: The conversation history (limited to the last 2 exchanges).
    :param model: The AI model to use for generating responses.
    :param retries: Number of retries in case of failure.
    :return: The response content or an error message.
    """
    while retries > 0:
        try:
            # Maintain a rolling memory of the last 2 exchanges
            if len(chat_history) > 4:
                chat_history = chat_history[-4:]

            # Add user query to the conversation history
            chat_history.append({'role': 'user', 'content': query})

            # Generate response
            response = ollama.chat(
                model=model,
                messages=[
                    {
                        'role': 'system',
                        'content': 'You are a Python and programming-focused assistant. '
                                   'Provide clear, concise, and helpful code snippets, primarily in Python. '
                                   'Always offer explanations, test data, and practical examples.'
                    }
                ] + chat_history
            )

            if response and 'message' in response:
                assistant_response = response['message'].get('content', 'No response content available.')

                # Add assistant response to the history
                chat_history.append({'role': 'assistant', 'content': assistant_response})

                return assistant_response, chat_history

        except Exception as e:
            print(f"Error occurred: {e}. Retrying... ({3 - retries + 1}/3)")
            retries -= 1

    return "Sorry, I couldn't process your request due to repeated failures.", chat_history


def chat_loop():
    """
    Continuous chat loop for interacting with a Python and programming-specific assistant.
    Maintains efficient memory and implements retry logic.
    """
    print("Welcome to the Python Assistant!")
    print(get_dynamic_greeting())
    print("Type your query below. Type 'exit' or 'quit' to end the chat.\n")

    chat_history = []  # Limited memory for the last 2 exchanges

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye, my brilliant friend! Keep coding and stay curious! 😊")
            break

        print("\nProcessing your query...\n")
        response, chat_history = generate_response(user_input, chat_history)

        print("Assistant:\n")
        dynamic_typing_effect(response)
        print("\n---\n")


# Entry point
if __name__ == "__main__":
    try:
        chat_loop()
    except KeyboardInterrupt:
        print("\nSession ended. See you next time!")
