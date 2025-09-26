# Chai Of Thought Prompting
from dotenv import load_dotenv
from openai import OpenAI
import requests
import os
from pydantic import BaseModel, Field
from typing import Optional

import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

def run_command(cmd: str):
    result = os.system(cmd)
    return result


def get_weather(city: str):
    url = f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is {response.text}"
    return "Something went wrong"
 

available_tool={
    "get_weather": get_weather,
    "run_command": run_command
}


SYSTEM_PROMPT = """
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of available tools.
    for every tool call wait for the observe step which is the output from the called tool. 
    Rules:
    - Strictly  Follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START (where user gives an input), PLAN(That can
    be multiple times) and finally OUTPUT (which is going to the displayed to the user).

    Output JSON Format:
    {"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content":"string". "tool":"string","input":"string" }

    Available Tools: 
    - get_weather(city: str): Takes city name as an input string and return the weather info about the city.
    - run_command(cmd: str): Takes a system linux command as string and executes the command on user's system and returns 

    Example 1:
    START: Hey, Can you solve 2 + 3 * 5 / 10
    PLAN: {"step": "PLAN": "content":"Seems like user is interested in math problem" }
    PLAN: { "step": "PLAN": "content": "looking at the problem, we should solve this using BODMAS method" }
    PLAN: { "step": "PLAN": "content": "Yes, The BODMAS is correct thing to be done here" }
    PLAN: { "step": "PLAN": "content": "first we must multiply 3 * 5 which is 15 "}
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 15 / 10 "}
    PLAN: { "step": "PLAN": "content": "We must perform divide that is 15 / 10 = 1.5"}
    PLAN: { "step": "PLAN": "content": "Now the new equation is 2 + 1.5"}
    PLAN: { "step": "PLAN": "content": "Now finally lets perform the add 3.5"}
    PLAN: { "step": "PLAN": "content": "Great, we have solved and finally left with 3.5 as ans"}
    OUTPUT: { "step": "OUTPUT": "content": "3.5"} 

    Example 2:
    START: What is the weather of Delhi?
    PLAN: {"step": "PLAN": "content":"Seems like user is interested in getting weather of Delhi in India" }
    PLAN: { "step": "PLAN": "content": "Lets see if we have any available tool from the list of available" }
    PLAN: { "step": "PLAN": "content": "Great, we have get_weather tool available for this query." }
    PLAN: { "step": "PLAN": "content": "I need to call get_weather tool for delhi as input for city"}
    PLAN: { "step": "TOOL": "tool": "get_weather","input":"delhi"}
    PLAN: { "step": "OBSERVE": "tool":"get_weather" ,"output":"The temp of delhi is cloudy with 20"}
    PLAN: { "step": "PLAN": "content": "Great, I got the weather info about delhi"}
    OUTPUT: { "step": "OUTPUT": "content": "The current weather in delhi is 20 C with some cloudy sky"}

"""

print("\n\n\n")

class MyOutputFormat(BaseModel):
    step: str = Field(...,description="The ID of the step. Example: PLAN, OUTPUT, TOOL")
    content: Optional[str] = Field(None, description="The optional string content for the step")
    tool: Optional[str] = Field(None, description="The ID of the tool to call.")
    input: Optional[str] = Field(None, description="The input params for the tool")

message_history = [
    { "role":"system","content": SYSTEM_PROMPT}
]

user_query = input("= ")
message_history.append({ "role":"user","content": user_query })

while True:
    response=client.chat.completions.parse(
    model="gemini-2.5-flash",
    response_format=MyOutputFormat,
    messages=message_history
    )

    raw_result=(response.choices[0].message.content)
    message_history.append({"role":"assistant","content": raw_result})

    # parsed_result= json.loads(raw_result)
    parsed_result = response.choices[0].message.parsed

    if parsed_result.step  == "START":
        print("Fire", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "TOOL":
        tool_to_call = parsed_result.get("tool")
        tool_input = parsed_result.get("input")
        print(f" : {tool_to_call} ({tool_input})")

        tool_response = available_tool[tool_to_call](tool_input)
        print(f" : {tool_to_call} ({tool_input}) = {tool_response}")
        message_history.append({"role":"developer","content": json.dumps(
            {"step":"OBSERVE","tool":tool_to_call,"input":tool_input,"output":tool_response}
        )})
        continue

    if parsed_result.get("step") == "PLAN":
        print("Brain", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("BOT", parsed_result.get("content"))
        break


