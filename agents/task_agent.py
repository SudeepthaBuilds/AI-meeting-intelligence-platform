import re

def extract_tasks(transcript):
    tasks = []

    keywords = ["will", "should", "complete", "finish", "submit"]

    for sentence in transcript.split("."):
        for keyword in keywords:
            if keyword in sentence.lower():
                tasks.append(sentence.strip())
                break

    if not tasks:
        return "No action items found."

    return "\n".join(tasks)