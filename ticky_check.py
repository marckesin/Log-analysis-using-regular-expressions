# #!/usr/bin/env python3

import csv
import re


def find_error_message(line):
    pattern = r"\s([A-Z]*)\s([\w\s']*\w).*\(([\w.]*)\)"
    try:
        result = re.search(pattern, line)
        return result
    except Exception as e:
        return e


def dict_to_csv(file, header, data):
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(data)


error_messages = {}
per_user = {}

with open("syslog.log") as logs, open("user_statistics.csv",
                                      "w") as file1, open(
                                          "error_message.csv", "w") as file2:
    for line in logs.readlines():
        line = line.strip()

        if find_error_message(line):
            message, message_content, username = find_error_message(
                line).groups()
            per_user[username] = per_user.get(
                username, dict(Username=username, ERROR=0, INFO=0))

            if message == "ERROR":
                error_messages[message_content] = error_messages.get(
                    message_content, dict(Error=message_content, Count=0))

                if message_content in error_messages:
                    error_messages[message_content]["Count"] += 1

                if username in per_user:
                    per_user[username][message] += 1
            else:
                if username in per_user:
                    per_user[username][message] += 1

    error_messages_sorted = sorted(error_messages.values(),
                                   key=lambda x: x["Count"],
                                   reverse=True)
    per_user_sorted = sorted(per_user.values(), key=lambda x: x["Username"])

    header1 = ["Username", "INFO", "ERROR"]
    header2 = ["Error", "Count"]
    dict_to_csv(file1, header1, per_user_sorted)
    dict_to_csv(file2, header2, error_messages_sorted)
