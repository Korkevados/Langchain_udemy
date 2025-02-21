from dotenv import load_dotenv
from typing import  Tuple
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_party.linkedin import scrape_linkedin_profile
from output_parsers import summary_parser,Summary

def ice_break_with(name:str)->Tuple[Summary,str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_url)

    summary_template = """
        given the information {information} about a person I want you to create:
        1. A short summary
        2. two interesting facts about them
        Use  information from Linkedin \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")

    chain = summary_prompt_template | llm | summary_parser

    res:Summary = chain.invoke(input={"information": linkedin_data})

    return res, linkedin_data.get("photoUrl")

if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Start")
    ice_break_with("Daniel Korkevados bgu")
