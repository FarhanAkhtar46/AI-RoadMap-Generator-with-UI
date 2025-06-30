from supervisor import RoadmapSupervisor
from pathlib import Path
import os
from dotenv import load_dotenv
import json
from conversation_agent import RoadmapConversationAgent

def main():
    # Load environment variables
    load_dotenv()
    
    # Ensure output directory exists
    Path("output/visualizations").mkdir(parents=True, exist_ok=True)

    # Use the conversation agent for interactive input
    agent = RoadmapConversationAgent()
    prompt = agent.next_prompt()
    while prompt:
        answer = input(prompt + " ")
        result = agent.handle_user_input(answer)
        if isinstance(result, dict):  # Roadmap result
            
            print(f"\nVisualizations saved to: {result.get('html_path', 'N/A')}")
            break
        else:
            prompt = result
            if prompt:
                print(prompt)

if __name__ == "__main__":
    main()