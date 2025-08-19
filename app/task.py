from dotenv import load_dotenv
import os
from crewai import Agent, Crew, Task, LLM
from agent import research, writer
load_dotenv()

llm = LLM(model="gpt-4o-mini", temperature=0.1, max_tokens=1000)
# Create tasks
research_task = Task(
    description="Research the latest advancements in {topic}",
    expected_output="A comprehensive 3 paragraph report on the latest trends",
    agent=research,
)

writer_task = Task(
    description="Write an engaging article based on the research findings about {topic}",
    expected_output="A well-written 3 paragraph article on the latest trends",
    agent=writer,
)
