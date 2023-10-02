import openai
from dotenv import load_dotenv
from colorama import init
from termcolor import colored
from baai_context.prompts import get_epic_prompt
from baai_context.prompts import get_story_prompt
from baai_context.prompts import get_ac_prompt

# Load environment variables from the .env file
load_dotenv()
init()
# models
GPT_35_TURBO_MODEL = "gpt-3.5-turbo"


def ba_agent(prompt):
    messages = [{"role": "user", "content": prompt}]
    completion = openai.ChatCompletion.create(
        model=GPT_35_TURBO_MODEL,
        temperature=0,
        messages=messages
    )
    return completion.choices[0].message.content


def display_menu():
    print(
        colored('\nWelcome you! I am BAAI (Business Analysis AI Assistant)', 'green'))
    print(colored('\n1. Generate Epics', 'cyan'))
    print(colored('2. Create Stories For Epic', 'cyan'))
    print(colored('3. Write Acceptance Criteria for a Story', 'cyan'))
    print(colored("Type 'quit' to exit the chat.\n",
                  'yellow', attrs=['bold']))


def handle_epic():
    epics = ba_agent(get_epic_prompt())
    print(colored(f"{epics}\n\n", 'light_yellow'))


def handle_story():
    userinput_epic = input("Enter Epic details: ")
    stories = ba_agent(get_story_prompt(userinput_epic))
    print(colored(f"{stories}\n", 'light_blue'))


def handle_acceptance_criteria():
    userinput_story = input("Enter Story details: ")
    acceptance_criterias = ba_agent(get_ac_prompt(userinput_story))
    print(colored(f"{acceptance_criterias}\n", 'light_magenta'))


if __name__ == "__main__":
    try:
        while True:
            display_menu()

            user_input = input("You: ")
            if user_input.lower() == 'quit':
                break
            elif user_input == '1':
                handle_epic()
            elif user_input == '2':
                handle_story()
            elif user_input == '3':
                handle_acceptance_criteria()
            else:
                print(colored("Your input was incorrect...", 'red'))
    except Exception as e:
        print(f"\nAn error occurred: {e}. Saving message history and exiting.")
