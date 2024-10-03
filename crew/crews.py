from crewai import Agent, Task, Crew


def get_cover_letter(name, client_name, job_title, profile, job_post, words):

    agent = Agent(
        role=job_title,
        goal='Apply for jobs',
        backstory="You are {name}, an experience and competent {job_title} looking for a job"
    )

    task = Task(
        description="This is your profile: {profile}, and with that profile you have to apply for this job post: {job_post} posting"
                    "by {client_name}",
        agent=agent,
        expected_output='Your application in its final version in no more than {words} words',
    )

    inputs = {
        "name": name,
        "job_title": job_title,
        "profile": profile,
        "job_post": job_post,
        "client_name": client_name,
        "words": words
    }

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True,
    )

    response = crew.kickoff(inputs=inputs).raw

    return response
