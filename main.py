import git
import os
import requests
import ollama


def read_code_from_repo(repo_path):
    repo = git.Repo(repo_path)
    files = []

    for root, dirs, filenames in os.walk(repo_path):
        for filename in filenames:
            if filename.endswith(".py"):  # Hier kannst du die Dateierweiterung anpassen
                with open(os.path.join(root, filename), "r") as f:
                    files.append(f.read())

    return files


def lint_ollama(code):
    response = ollama.chat(
        model="gemma2",
        messages=[
            {
                "role": "system",
                "content": "can you give some hints for the code, how to write it better or if you see potential bugs, please provide a short list of hints with numbers",
            },
            {
                "role": "user",
                "content": code,
            },
        ],
    )
    print(response["message"]["content"])


files = read_code_from_repo(
    "/Users/beholzer/Documents/projects/github.com/b3rtram/trubby"
)

for file in files[0:1]:
    lint_ollama(file)
