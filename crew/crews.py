from crewai import Agent, Task, Crew

def get_agent_that_match_skills_with_job(profile, job_post, symbol="<>"):

    agent = Agent(
        role="Senior Talent Acquisition Specialist",
        goal='Identify skills in people',
        backstory="You are a competent Senior Talent Acquisition Specialist with highly oriented to details,"
                  "and capable to identify talent and skills in people"
    )

    task = Task(
        description="List your the accomplishments, qualifications, and anything that makes the candidate with"
                    "this {profile} stand out among the crowd and everyone should know about him or her and at the"
                    "same time match with the requirements that this job post: {job_post} creating points of contacts"
                    "between the candidate and the job",
        agent=agent,
        expected_output='A bullet list summary of the top 5 most important skills. Writen in first person.'
                        'When finish put this symbol: {symbol}',
    )

    inputs = {
        "profile": profile,
        "job_post": job_post,
        "symbol": symbol
    }

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    response = crew.kickoff(inputs=inputs).raw
    print(response)
    return response.replace("my best complete final answer to the task.", "").replace(symbol, "")

def get_agent_that_find_contribution(profile, job_post, symbol="<>"):

    agent = Agent(
        role="Senior Talent Acquisition Specialist",
        goal='Identify skills in people',
        backstory="You are a competent Senior Talent Acquisition Specialist with highly oriented to details,"
                  "and capable to identify talent and skills in people"
    )

    task = Task(
        description="Describe how a canditate with this profile {profile} can bring value to this job, based in"
                    "this job description {job_post}",
        agent=agent,
        expected_output='A text of three lines. Writen in first person.'
                        'When finish put this symbol: {symbol}',
    )

    inputs = {
        "profile": profile,
        "job_post": job_post,
        "symbol": symbol
    }

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    response = crew.kickoff(inputs=inputs).raw
    print(response)
    return response.replace("my best complete final answer to the task.", "").replace(symbol, "")