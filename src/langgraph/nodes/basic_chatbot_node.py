from src.langgraph.state.state import State


class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self, model):
        self.llm=model 
    
    def process(self, state) -> dict:
        """
        Processes the input state and generates a chatbot response.
        """
        return {"messages":self.llm.invoke(state['messages'])}