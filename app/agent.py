from dotenv import load_dotenv
import os
from crewai import Agent, Crew, Task, LLM

load_dotenv()

llm = LLM(model="gpt-4o-mini", temperature=0.1, max_tokens=1000)

# Create agents without tools first
research = Agent(
    role="Senior Researcher",
    goal="Uncover groundbreaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory="Driven by curiosity, you are at the forefront of innovation, eager to explore and share knowledge that could change the world",
    llm=llm,
)

writer = Agent(
    role="Senior Writer", 
    goal="Write a comprehensive article on {topic}",
    verbose=True,
    memory=True,
    backstory="You are a seasoned writer with a passion for storytelling and a knack for captivating readers. Your articles are not just informative but also engaging, making complex topics accessible to a wide audience.",
    llm=llm,
)
