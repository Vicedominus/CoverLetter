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


def get_cover_letter(name, client_name, job_title, profile, job_post, symbol="<>"):

    agent = Agent(
        role=job_title,
        goal='Apply for jobs',
        backstory="You are {name}, an experience and competent {job_title} looking for a job"
    )

    task = Task(
        description="This is your profile: {profile}, and with that profile you have to apply for this job post: {job_post} posting"
                    "by {client_name}",
        agent=agent,
        expected_output='Your application in its final version in no more than 200 words',
    )

    inputs = {
        "name": name,
        "job_title": job_title,
        "profile": profile,
        "job_post": job_post,
        "client_name": client_name
    }

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    response = crew.kickoff(inputs=inputs).raw
    print(response)
    return response