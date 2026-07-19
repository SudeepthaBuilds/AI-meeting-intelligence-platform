from django.shortcuts import render
from .forms import MeetingForm

from agents.transcriber import transcribe_audio
from agents.summary_agent import generate_summary
from agents.parser import parse_response


def upload_meeting(request):

    if request.method == "POST":

        form = MeetingForm(request.POST, request.FILES)

        if form.is_valid():

            meeting = form.save()

            transcript = transcribe_audio(meeting.audio.path)
            ai_response = generate_summary(transcript)

            summary, key_points, action_items, next_steps = parse_response(ai_response)

            return render(
                request,
                "meetings/results.html",
                {
                    "transcript": transcript,
                    "summary": summary,
                    "key_points": key_points,
                    "action_items": action_items,
                    "next_steps": next_steps,
                },
            )

    else:

        form = MeetingForm()

    return render(request, "meetings/upload.html", {"form": form})


def meeting_list(request):

    return render(request, "meetings/list.html")