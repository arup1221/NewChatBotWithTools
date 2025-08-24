import streamlit as st
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraph.LLMs.groqllm import GroqLLM
from src.langgraph.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraph.graph.graph_builder import GraphBuilder
from src.langgraph.ui.streamlitui.display_result import DisplayResultStreamlit

def load_langgraph_agentical_app():
    """
    Loads and runs the LangGraph AgenticAI application with StremlitUI. This function initilizes the UI, handles user input, configures the LLM model, sets up the graph based on the selected use case, and displays the output while implementing exception handling for robustness.
    
    """
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error: Failed to load user input form the UI.")
        return
    
    user_message = st.chat_input("Enter your message: ")
    
    if user_message:
        try:
            obj_llm_config=GroqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error: LLM model could not be initilized")
                return
            
            usecase=user_input.get("selected_usecase")
            
            if not usecase:
                st.error("Error: No use case selected.")
                return
            
            #graph builder
            graph_builder=GraphBuilder(model)
            try:
                graph=graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase, graph, user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed - {e}")
                return
            
            
        except Exception as e:
             st.error(f"Error: Graph set up failed - {e}")
             return
    