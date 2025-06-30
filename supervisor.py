from typing import Dict, Any
from pathlib import Path  # Add this import
from base_agent import BaseAgent  # Change to absolute import
from domain_agent import DomainAgent
from roadmap_agent import RoadmapAgent
from visualization_agent import VisualizationAgent
from visualization_renderer import VisualizationRenderer

class RoadmapSupervisor:
    def __init__(self):
        self.domain_agent = DomainAgent()
        self.roadmap_agent = RoadmapAgent()
        self.visualization_agent = VisualizationAgent()
        self.renderer = VisualizationRenderer()
    
    def generate_roadmap(self, user_input: str) -> Dict[str, Any]:
        
        # Step 1: Domain clarification
        domain_result = self.domain_agent.process({"user_input": user_input})
        print(user_input)

        if domain_result["status"] != "success":
            return {"error": "Domain clarification failed"}
        
        # Step 2: Roadmap generation
        roadmap_result = self.roadmap_agent.process({
            "domain_info": domain_result["domain_info"]
        })

        visualization_result = self.visualization_agent.process({
            "roadmap": roadmap_result["roadmap"]
        })
        
        # Generate HTML page with all visualizations
        html_content = self.renderer.render_html(
            visualization_result["visualizations"]["mermaid"]["content"],  # Mermaid content
            
            visualization_result["visualizations"]["mindmap"]["content"]
        )
        
        # Save the HTML page
        output_path = Path("output/roadmap.html")
        self.renderer.save_visualization(html_content, str(output_path))
        
        return {
            "status": "success",
            "domain_info": domain_result["domain_info"],
            "roadmap": roadmap_result["roadmap"],
            "visualizations": visualization_result["visualizations"],
            "html_path": str(output_path)
        }
    