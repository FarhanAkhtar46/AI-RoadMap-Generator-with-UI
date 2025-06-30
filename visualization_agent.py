from typing import Dict, Any, List
from base_agent import BaseAgent

import json
from pathlib import Path
from langchain.tools import Tool
from datetime import datetime



class VisualizationAgent(BaseAgent):
    def _initialize_tools(self):
        self.tools = [
            
            Tool(
                name="generate_mermaid",
                func=self.generate_mermaid,
                description="Generates Mermaid.js diagram"
            )
        ]
        
        # Create output directory if it doesn't exist
        self.output_dir = Path("output/visualizations")
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def process(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        roadmap = input_data["roadmap"]
        domain_name = input_data.get("domain_name", "roadmap").replace(" ", "_").lower()

        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Generate all visualization types
        
        mermaid_result = self.generate_mermaid(roadmap)
        mindmap_result = self.generate_mindmap_mermaid(roadmap)
        
        # Save visualizations to files
        
        mermaid_path = self.output_dir / "roadmap.mmd"
        mindmap_path = self.output_dir / "roadmap_mindmap.mmd"
        
        
        
        with open(mermaid_path, "w") as f:
            f.write(mermaid_result)
        with open(mindmap_path, "w") as f:
            f.write(mindmap_result)

        # # Create and render Graphviz visualization
        # dot = graphviz.Source(graphviz_result)
        # dot.render(filename=str(jpeg_path.with_suffix('')), format='jpg', cleanup=True)
        
        
        return {
            "status": "success",
            "visualizations": {
                "mermaid": {
                    "file_path": str(mermaid_path),
                    "content": mermaid_result
                },
                "mindmap": {
                    "file_path": str(mindmap_path),
                    "content": mindmap_result
                }
            }
            
        }
    
    
    
    def generate_mermaid(self, roadmap: Dict[str, Any]) -> str:
        """Generate a Mermaid.js diagram of the roadmap"""
        mermaid_lines = ["graph LR"]
        
        # Add nodes
        for i, module in enumerate(roadmap["modules"]):
            node_id = f"module_{i}"  # Use index instead of id
            node_label = f"{module['name']}"
            if 'duration' in module:
                node_label += f" ({module['duration']})"
            mermaid_lines.append(f"    {node_id}[\"{node_label}\"]")
        
        # Add edges
        for i, module in enumerate(roadmap["modules"]):
            for dep in module.get('dependencies', []):
                # Find the index of the dependency module
                dep_index = next((i for i, m in enumerate(roadmap['modules']) 
                                if m['name'] == dep), None)
                if dep_index is not None:
                    mermaid_lines.append(f"    module_{dep_index} --> module_{i}")
        
        return "\n".join(mermaid_lines)
    
    def generate_mindmap_mermaid(self, roadmap: Dict[str, Any]) -> str:
        """Generate a Mermaid mindmap diagram of the roadmap"""
        lines = ["mindmap"]
        title = roadmap.get('title', 'Learning Roadmap')
        lines.append(f"  {title}")
        for module in roadmap.get('modules', []):
            lines.append(f"    {module['name']}")
            for topic in module.get('topics', []):
                lines.append(f"      {topic}")
        return "\n".join(lines)
    
    def _create_interactive_tooltip(self, module: Dict[str, Any]) -> str:
        """Create HTML tooltip content for a module"""
        return f"""
        <div class='tooltip'>
            <h3>{module['name']}</h3>
            <p><strong>Duration:</strong> {module['time_estimate']}</p>
            <p><strong>Resources:</strong></p>
            <ul>
                {self._format_resources(module.get('resources', []))}
            </ul>
        </div>
        """
    
    def _format_resources(self, resources: List[Dict[str, str]]) -> str:
        """Format resources as HTML list items"""
        return "\n".join([
            f"<li><a href='{r['url']}'>{r['title']}</a></li>"
            for r in resources
        ])