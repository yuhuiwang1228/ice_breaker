from dotenv import load_dotenv

load_dotenv()

from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent

def ice_break_with(name: str) -> str:
    linkedin_url = linkedin_lookup_agent(name=name)
    print(f"linkedin url: {linkedin_url}")
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url)
    print(f"linkedin url: {linkedin_data}")
    
    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = summary_prompt_template | llm # LLMChain(llm=llm, prompt=summary_prompt_template)
    
    # linkedin_data = scrape_linkedin_profile(
    #     linkedin_profile_url="https://www.linkedin.com/in/eden-marco/"
    # )
    res = chain.invoke(input={"information": linkedin_data})

    return res.content

if __name__ == "__main__":
    print(ice_break_with(name="Eden Marco Udemy"))
