from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    print("Inside chatbot node", state)
    return { "messages": ["Hi, This is a message from ChatBot Node"]}

def samplenode(state: State):
    return { "messages": ["Sample Message Appended"]}

graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge(chatbot, "samplenode")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

# (START) -> chatbot -> samplenode -> (END)

# state = { messages: ["Hey there"]}
# node runs: chatbot(state: ["Hey There"])  -> ["Hi, This is a message from ChatBot Node"]
# state = { "messages": ["Hey there", "Hi, This is a message from ChatBot Node"]}

