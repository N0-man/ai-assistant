# imports
import openai  # for calling the OpenAI API
import os
import json
from datetime import datetime
from dotenv import load_dotenv
from document_embedding import doc_agent
from colorama import init
from termcolor import colored

# Load environment variables from the .env file
load_dotenv()
init()


def write_message_history_to_file(full_message_history, directory):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f"message_history_{timestamp}.json"
    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    with open(file_path, 'w') as outfile:
        json.dump(full_message_history, outfile, indent=2)


def execute():
    try:
        print(colored('Welcome to the Context based AI Assistant interface!', 'green'))
        print(colored("Type 'quit' to exit the chat.\n",
              'yellow', attrs=['bold']))
        message_history = []
        full_message_history = []
        max_history = 100  # Adjust this value to limit the number of messages considered

        while True:
            user_input = input("You: ")
            if user_input.lower() == 'quit':
                write_message_history_to_file(
                    full_message_history, "./message_logs")
                break
            else:
                message_history.append({"role": "user", "content": user_input})
                full_message_history.append(
                    {"role": "user", "content": user_input})

                # reduces messages when max history exceeded
                if len(message_history) > max_history:
                    # Keep the system message and remove the second message
                    message_history = [message_history[0]] + \
                        message_history[-(max_history - 1):]

                # Check user input, if executive is needed, call executive on user input and return result.
                agent_response = doc_agent(message_history[-1].get("content"))
                print(colored("\nAI response", 'yellow', attrs=['bold']))
                print(colored(f"{agent_response}\n", 'green'))

    except KeyboardInterrupt:
        print("\nDetected KeyboardInterrupt. Saving message history and exiting.")
    except Exception as e:
        print(f"\nAn error occurred: {e}. Saving message history and exiting.")
    finally:
        write_message_history_to_file(full_message_history, "./message_logs")
        print("Message history saved.")


if __name__ == "__main__":
    execute()
