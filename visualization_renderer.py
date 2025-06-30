from typing import Dict, Any
import json
from pathlib import Path
from langchain.tools import Tool

class VisualizationRenderer:
    def render_html(self, mermaid_content: str, mindmap_content: str) -> str:
        # Clean up the mermaid and mindmap content
        mermaid_content = mermaid_content.strip()
        mindmap_content = mindmap_content.strip()
        
        # Create HTML template with proper Mermaid.js initialization
        html_template = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Learning Roadmap Visualization</title>
            <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
            <script>
                mermaid.initialize({{
                    startOnLoad: true,
                    theme: 'default',
                    securityLevel: 'loose',
                    flowchart: {{
                        useMaxWidth: false,
                        htmlLabels: true
                    }}
                }});
            </script>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .container {{ display: flex; flex-direction: column; gap: 20px; }}
                .visualization {{ border: 1px solid #ccc; padding: 20px; border-radius: 5px; }}
                h2 {{ color: #333; }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="visualization">
                    <h2>Mermaid.js Visualization</h2>
                    <div class="mermaid">
                    {mermaid_content}
                    </div>
                </div>
                <div class="visualization">
                    <h2>Mind Map (Mermaid.js)</h2>
                    <div class="mermaid">
                    {mindmap_content}
                    </div>
                </div>
                
            </div>
        </body>
        </html>
        """
        return html_template

    def save_visualization(self, html_content: str, output_path: str):
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)