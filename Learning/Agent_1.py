# maling a chatbot with a memeory 

import os
from typing import TypedDict, List, Union
from langchain_core.messages import HumanMessage,AIMessage  # In built datatypes 
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages : List[Union[HumanMessage,AIMessage]] # HumanMessgae and AIMessage are datatpe in the langchain and langgraph

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

def process(state: AgentState)-> AgentState:
    """ This Node will reply to the Human"""
    response = llm.invoke(state["messages"])

    state["messages"].append(AIMessage(content =  response.content))

    print(f"\n AI : {response.content}")
    print("Current State : ", state["messages"])

    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()

converstion_History = []


user_input = input("Enter Something : ")

while(user_input != "exit"):

    converstion_History.append(HumanMessage(content=user_input))

    result = agent.invoke({"messages" : converstion_History})

    # print(result["messages"])
    converstion_History = result["messages"]

    user_input = input("Enter Something : ")