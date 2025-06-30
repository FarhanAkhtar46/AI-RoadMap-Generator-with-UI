from typing import Dict, Any
from base_agent import BaseAgent
from langchain.tools import Tool

class RoadmapAgent(BaseAgent):
    def _initialize_tools(self):
        self.tools = [
            Tool(
                name="generate_roadmap",
                func=self.generate_roadmap,
                description="Generates a structured learning roadmap"
            )
        ]
    
    def generate_roadmap(self, domain_info: Dict[str, Any]) -> Dict[str, Any]:
        prompt = f"""Generate a detailed learning roadmap based on:
        Domain: {domain_info['primary_domain']}
        Level: {domain_info['knowledge_level']}
        Objectives: {domain_info['learning_objectives']}
        
        Provide a structured JSON with:
        - modules: List of learning modules with dependencies
        - time_estimates: Estimated duration for each module
        - resources: Recommended learning resources
        - prerequisites: Required knowledge for each module
        """
        
        response = self.llm.invoke(prompt)
        return self._parse_response(response)
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        roadmap = self.generate_roadmap(input_data["domain_info"])
        return {
            "status": "success",
            "roadmap": roadmap
        }
    
    