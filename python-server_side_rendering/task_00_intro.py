#!/usr/bin/python3
"""Generate personalized invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files using a template and attendee data."""
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
            isinstance(attendee, dict) for attendee in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = (
        "name",
        "event_title",
        "event_date",
        "event_location"
    )

    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for placeholder in placeholders:
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            invitation = invitation.replace(
                "{" + placeholder + "}", str(value)
            )

        filename = f"output_{index}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(invitation)