def parse_response(text):

    summary = ""
    key_points = []
    action_items = []
    next_steps = []

    current = ""

    for line in text.split("\n"):

        line = line.strip()

        if line.startswith("SUMMARY"):
            current = "summary"
            continue

        elif line.startswith("KEY POINTS"):
            current = "key"
            continue

        elif line.startswith("ACTION ITEMS"):
            current = "action"
            continue

        elif line.startswith("NEXT STEPS"):
            current = "next"
            continue

        if line == "":
            continue

        if current == "summary":
            summary += line + " "

        elif current == "key":
            key_points.append(line.replace("-", "").strip())

        elif current == "action":
            action_items.append(line.replace("-", "").strip())

        elif current == "next":
            next_steps.append(line.replace("-", "").strip())

    return summary, key_points, action_items, next_steps