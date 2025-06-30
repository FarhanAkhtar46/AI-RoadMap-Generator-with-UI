from abc import ABC, abstractmethod
from typing import Dict, Any
from langchain_community.chat_models import ChatOpenAI  # Updated import
from langchain.tools import Tool
import json
import re

class BaseAgent(ABC):
    def __init__(self, model_name: str = "gpt-4o", temperature: float = 0.7):
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.tools = []
        self._initialize_tools()
    
    @abstractmethod
    def _initialize_tools(self):
        """Initialize agent-specific tools"""
        pass
    
    @abstractmethod
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process input data and return results"""
        pass


    def _parse_response(self, response: str) -> Dict[str, Any]:
        try:
            # Get the content from the AIMessage if it's not already a string
            content = response.content if hasattr(response, 'content') else response
            
            # Try to parse the response as JSON
            return json.loads(content)
        except json.JSONDecodeError:
            # If parsing fails, try to extract JSON from the text
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            raise ValueError("Could not parse response as JSON")
            