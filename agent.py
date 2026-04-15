from groq import Groq
from automation import run_steps
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_steps(task):
    prompt = f"""
You are an IT automation agent for a VERY SIMPLE admin panel.

The panel ONLY supports:
1. open site
2. create user <email>
3. reset password <email>

Convert the task into ONLY these steps.

Rules:
- ONLY output steps from the allowed list
- NO extra steps
- NO explanation
- NO numbering
- NO words like authenticate, navigate, verify

Examples:

Task: create user john@company.com
Output:
open site
create user john@company.com

Task: reset password for john@company.com
Output:
open site
reset password john@company.com

Now convert:

Task: {task}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content

    steps = output.split("\n")
    return [s.strip().lower() for s in steps if s.strip()]


def run_agent(task):
    print("\n User Task:", task)

    steps = get_steps(task)

    print("\n Agent Plan:")
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")

    print("\n Executing...\n")

    run_steps(steps)


if __name__ == "__main__":
    task = input("Enter task: ")
    run_agent(task)