from baai_context.br import product_high_level_requirement

epic_story_ac_structure = {
    "epic": {
        "definition": "An epic is a large body of work that can be broken down into a number of smaller user stories.",
        "format": {
            "structure": "<Epic-Heading> : <Description>",
            "example": "Login : Login for new visitors"
        },
        "example": "The epic for a search functionality in a music app can be written as '''The new search functionality will allow users to narrow down their search and offer suggestions to help them find the music they want to listen to instantly.'''"
    },
    "story": {
        "definition": "A user story is a small, self-contained unit of development work designed to accomplish a specific goal within a product. It provides an informal, natural language description of a feature of the software or product from the end-user perspective.",
        "template": "As a < type of user >, I want < some goal > so that < some reason >.",
        "format": {
            "structure": "<User-Story-Number> - <User-Story-Heading> : <User-Story>",
            "example": "GT-Recruit-101 - Post resume to website : \
                        A user can post her resume to the web site so employers can be informed \
                        about the work details about the user."
        },
        "example": "A few real examples of user stories that describe the desired functionality in an early version of the Scrum Alliance website are below: \
            1. As a site member, I can fill out an application to become a Certified Scrum Trainer so that I can teach Certified Scrum Master and Certified Scrum Product Owner courses and certify others.\
            2. As a trainer, I want my profile to list my upcoming classes and include a link to a detailed page about each so that prospective attendees can find my courses.\
            3. As a site visitor, I can access old news that is no longer on the home page, so I can access things I remember from the past or that others mention to me.\
            4. As a site visitor, I can see a list of all upcoming “Certification Courses” and can page through them if there are a lot, so I can choose the best course for me."
    },
    "acceptance-criteria": {
        "definition": "A set of statements, each with a clear pass/fail result, that specify both functional and non-functional requirements and are applicable at the feature and story levels.",
        "template": "Given <what all are the given conditions>, when <a particular action taken>, then <the result of that action>.",
        "format": {
            "structure": "<List of acceptance criterias>"
        },
        "example": "Few real examples of acceptance criterias for a user story '''As a user, I want to be able to recover the password to my account so that I can access it in case I forget it. ''' are below:\
        1. Given The user is logged out When the user navigates to the login page, they see the 'forgot password' option.\
        2. Given The user navigates to the login page When the user selects the 'forgot password' option and enters a valid email to receive a link for password recovery, the system sends the link to the entered email.\
        3. Given The user receives the link via the email When The user navigates through the link received in the email Then The system enables the user to set a new password"

    }
}


def get_epic_prompt():
    return f"""

    Epic = {epic_story_ac_structure["epic"]["definition"]}

    Example for an epic : {epic_story_ac_structure["epic"]["example"]}

    Your task is to perform the following actions: 
    1. Analyse each of the features listed to determine the various high-level epics.
    2. List each epic.
    3. Describe each epic in a few sentences.

    Use the following format:
    Feature: <Feature Heading>
    Feature Summary: <Feature Description>
    Epics: List of Epics in the Format: '''epic_story_ac_structure["epic"]["format"]["structure"]'''>. Format example: '''{epic_story_ac_structure["epic"]["format"]["example"]}'''

    Text: <{product_high_level_requirement}>
    """


def get_story_prompt(epic_details):
    return f"""
    User-Story = {epic_story_ac_structure["story"]["definition"]}

    When writing a user-story, follow the standard format mentioned with text delimited by triple 
    quotes.
    '''{epic_story_ac_structure["story"]["template"]}'''

    User-Story-Number = '''STORY-<Project short name for 'Epic-Heading'>-<Story-Number>\n'''
    Example for a user-story : {epic_story_ac_structure["story"]["example"]}

    Your task is to perform the following actions:
    1. Analyse the epic and break it down further into various user stories.
    2. List the epic in the below format:
        <Feature>
        <Epic-Heading>
    3. List out detailed user stories in each of the epics in the below format: 
        <User-Story-Number> - <5 worded title for the user story> : <User-Story>

    Text: <{epic_details}>
    """


def get_ac_prompt(story_details):
    return f"""
    Acceptance-Criteria = {epic_story_ac_structure["acceptance-criteria"]["definition"]}

    When writing acceptance-criteria, follow the standard format mentioned with text delimited by triple 
    quotes.
    '''{epic_story_ac_structure["acceptance-criteria"]["template"]}'''

    Example for a acceptance-criteria : {epic_story_ac_structure["acceptance-criteria"]["example"]}

    Your task is to perform the following actions:
    1. Analyse the given user story and list down acceptance criterias in the below format:
        Acceptance Criteria : <Acceptance-Criteria>

    Text: <{story_details}>
    """
