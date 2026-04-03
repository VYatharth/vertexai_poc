from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    instruction="When asked about a topic, summarize the answer in 5 bullet points and provide a 6 lines crisp summary at the end",
    description="An agent that helps with history lessions",
)
