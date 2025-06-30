from typing import Dict, Any
from base_agent import BaseAgent
from langchain.tools import Tool

class DomainAgent(BaseAgent):
    def _initialize_tools(self):
        self.tools = [
            Tool(
                name="analyze_domain",
                func=self.analyze_domain,
                description="Analyzes the learning domain and requirements"
            )
        ]
    
    def analyze_domain(self, user_input: str) -> Dict[str, Any]:
        prompt = f"""Analyze the following learning request and provide structured information:
        {user_input}
        
        Return a JSON object with these exact keys:
        - primary_domain: The main field of study
        - knowledge_level: Current level (beginner/intermediate/advanced)
        - learning_objectives: List of specific goals
        - time_constraint: Any time constraints mentioned
        - prerequisites: Required background knowledge
        """
        
        response = self.llm.invoke(prompt)
        return self._parse_response(response)
    
    def process(self, input_data: str) -> Dict[str, Any]:
        domain_info = self.analyze_domain(input_data)
        return {
            "status": "success",
            "domain_info": domain_info
        }