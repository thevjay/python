from dotenv import load_dotenv
from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.mongodb import MongoDBSaver

load_dotenv()

llm = init_chat_model(
    model="gpt-4.1-mini",
    model_provider="openai"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    print("Inside chatbot node", state)
    response = llm.invoke(state.get("messages"))
    return { "messages": [response]}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("samplenode", END)

graph = graph_builder.compile()

def compile_graph_with_checkpointer(checkpointer):
        return graph_builder.compile(checkpointer=checkpointer)

DB_URI = "mongodb://admin:admin@localhost:27017/lg"
with MongoDBSaver.from_conn_string(DB_URI) as checkpointer:
    graph_with_checkpointer = compile_graph_with_checkpointer(checkpointer=checkpointer)

    config = {
        "configurable":{
            "thread_id": "vijay"  # user_idf
        }
    }
f
    for chunk in graph_with_checkpointer.stream(
        State({"messages":["what is my name? && You know that I am learf ning Langgraph"]}),
        config,
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()

    # updated_state = graph_with_checkpointer.invoke(
    #     State({"messages":["Hi, My name is vijay"]}),
    #     config,
    #     )
    # print("\n\nupdated_state", updated_state)

# Checkpointer (vijay) = Hey , My name is vijay