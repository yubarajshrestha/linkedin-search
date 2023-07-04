from services.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup import lookup
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate


# Create a prompt template
summary = """
    given the linkedin information {information} about a person from I want you to create:
    - a short summary of the person
    - eduction history
    - work history
"""
prompt_template = PromptTemplate(
    input_variables=["information"],
    template=summary,
)

# Create a prompt chain
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
prompt = LLMChain(llm=llm, prompt=prompt_template)


def queryInformation(person_name: str):
    linkedin_profile_url = lookup(name=person_name)
    information = scrape_linkedin_profile(linked_profile_url=linkedin_profile_url)

    return prompt.run(information=information)
