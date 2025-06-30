from supervisor import RoadmapSupervisor

class RoadmapConversationAgent:
    def __init__(self):
        self.questions = [
            {"key": "domain", "prompt": "What domain would you like a roadmap for?"},
            {"key": "expertise", "prompt": "What is your current expertise in this domain? (Beginner, Intermediate, Expert)"},
            {"key": "purpose", "prompt": "Why do you want to learn this? (Job, Education, Teaching, etc.)"},
            {"key": "timeframe", "prompt": "What is your desired timeframe for learning? (e.g., 4, 12, or 24 weeks)"},
            {"key": "goal", "prompt": "Do you have a specific goal? (e.g., develop a project, integrate into an application, etc.)"}
        ]
        self.answers = {}
        self.current_question = 0
        self.roadmap_result = None
        self.supervisor = RoadmapSupervisor()

    def next_prompt(self):
        if self.current_question < len(self.questions):
            return self.questions[self.current_question]["prompt"]
        return None

    def handle_user_input(self, user_input):
        if self.current_question < len(self.questions):
            key = self.questions[self.current_question]["key"]
            self.answers[key] = user_input
            self.current_question += 1
            if self.current_question < len(self.questions):
                return self.questions[self.current_question]["prompt"]
            else:
                # All answers collected, generate roadmap
                user_input_structured = self._format_user_input()
                self.roadmap_result = self.supervisor.generate_roadmap(user_input_structured)
                return self.roadmap_result
        else:
            return self.roadmap_result or "Conversation complete."

    def _format_user_input(self):
        # Combine all answers into a single string or dict as expected by supervisor
        # Here, we use a formatted string for compatibility with DomainAgent
        return (
            f"Domain: {self.answers.get('domain', '')}\n"
            f"Expertise: {self.answers.get('expertise', '')}\n"
            f"Purpose: {self.answers.get('purpose', '')}\n"
            f"Timeframe: {self.answers.get('timeframe', '')}\n"
            f"Goal: {self.answers.get('goal', '')}"
        ) 