from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import pytest
import logging

logger = logging.getLogger(__name__)

@pytest.mark.requires("openai")
def test_llm(init_server: str):
    llm = ChatOpenAI(openai_api_key="YOUR_API_KEY", openai_api_base=f"{init_server}/openai/v1")
    template = """Question: {question}
    
    Answer: Let's think step by step."""

    prompt = PromptTemplate.from_template(template)

    llm_chain = LLMChain(prompt=prompt, llm=llm)
    responses = llm_chain.run("你好")
    logger.info("\033[1;32m" + f"llm_chain: {responses}" + "\033[0m")

