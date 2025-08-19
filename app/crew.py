from dotenv import load_dotenv
import os
from crewai import Agent, Crew, Task, LLM
from agent import research, writer
from task import research_task, writer_task
load_dotenv()

llm = LLM(model="gpt-4o-mini", temperature=0.1, max_tokens=1000)


crew = Crew(
    agents=[research, writer],
    tasks=[research_task, writer_task],
    llm=llm,
    verbose=True,
    memory=True
)

# Execute crew
if __name__ == "__main__":
    result = crew.kickoff(inputs={"topic": "healthcare AI"})
    print(result)