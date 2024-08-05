
def get_intro():
    return ("Thank you very much for sharing comprehensive details about your job. It immediately "
            "caught my interest and aligned perfectly with my background as a ")

def get_mention_profile():
    return ("As you can see on my Upwork profile, I’ve completed numerous jobs with 5-star reviews "
            "and highly positive client feedback.")

def get_examples_pitch(examples, examples_related):
    if examples is not None:
        example_list = ''
        for example in examples:
            example_list += f" - {example} \n"

        if examples_related:

            pitch = get_mention_profile() + (" I've included two specific examples in this proposal "
                                             "that demonstrate the quality of my work and directly relate "
                                             "to your job post. \n") + example_list + "\n"
        else:
            pitch = get_mention_profile() + (" I've included two specific examples in this proposal "
                                             "that demonstrate the quality of my work. \n") + example_list + "\n"
    else:
        pitch = get_mention_profile() + "\n"
    return pitch
