from .transcript_agent import generate_transcript
from .summary_agent import generate_summary
from .task_agent import extract_tasks

def process_meeting(meeting):
    transcript = generate_transcript(meeting.audio.path)

    summary = generate_summary(transcript)

    tasks = extract_tasks(transcript)

    meeting.transcript = transcript
    meeting.summary = summary
    meeting.action_items = tasks

    meeting.save()