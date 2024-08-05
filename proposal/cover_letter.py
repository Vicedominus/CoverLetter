from .constants import get_intro, get_examples_pitch
from crew.crews import get_agent_that_match_skills_with_job, get_agent_that_find_contribution


class CoverLetter(object):

    def __init__(self, client_name, job_title, examples, examples_related, profile, job_post, call, name):
        self.client_name = client_name
        self.job_title = job_title
        self.examples = examples
        self.examples_related = examples_related
        self.profile = profile
        self.job_post = job_post
        self.call = call
        self.name = name

    def intro(self):
        if self.client_name is None:
            greet = 'Hi! '
        else:
            greet = f'Hi {self.client_name}! '

        return greet + get_intro() + self.job_title + ". \n\n"

    def work_examples(self):
        return get_examples_pitch(self.examples, self.examples_related)

    def about_me(self):
        head_line = "Here’s what you should know about me: \n"
        skills_for_job = get_agent_that_match_skills_with_job(self.profile, self.job_post)

        return head_line + skills_for_job + " \n"

    def my_contribution_to_the_project(self):
        head_line = "Here’s what I can bring to your project: \n"
        contribution_for_job = get_agent_that_find_contribution(self.profile, self.job_post)

        return head_line + " \n" + contribution_for_job + " \n"

    def call_to_action(self):
        if self.call:
            return ("\n Let's schedule a quick 10-minute introductory call to go over your project in more detail and "
                    "ensure I am the perfect fit for your needs. \n")
        else:
            return ("\n Let's chat to discuss your project in more detail and ensure I am the perfect fit for your "
                    "needs. \n")

    def closing(self):
        return (f"\n I am eager to hear more about your exciting project and how I can assist you! \n "
                f"\n Best Regards, {self.name}.")