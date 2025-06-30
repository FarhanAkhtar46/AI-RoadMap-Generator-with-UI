import openai

class DynamicLLMConversationAgent:
    def __init__(self, openai_api_key, model="gpt-4o"):
        self.history = []
        self.openai_api_key = openai_api_key
        self.model = model
        self.client = openai.OpenAI(api_key=openai_api_key)

    def handle_user_input(self, user_input):
        self.history.append({"role": "user", "content": user_input})

        # Compose the prompt for the LLM
        prompt = self._build_prompt()

        # Call OpenAI API (new style)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=prompt,
            temperature=0.7,
        )

        assistant_message = response.choices[0].message.content
        self.history.append({"role": "assistant", "content": assistant_message})

        # Decide if it's time to generate the roadmap
        if "[GENERATE_ROADMAP]" in assistant_message:
            user_profile = self._extract_profile()
            from supervisor import RoadmapSupervisor
            supervisor = RoadmapSupervisor()
            roadmap_result = supervisor.generate_roadmap(user_profile)
            return roadmap_result
        else:
            return assistant_message

    def _build_prompt(self):
        system_prompt = {
            "role": "system",
            "content": (
                "You are an expert learning roadmap assistant. "
                "Ask the user one question at a time to clarify their needs for a tailored learning roadmap. "
                "Ask about expertise, purpose, timeframe, tech stack, and any other relevant details. "
                "When you have enough information, reply with [GENERATE_ROADMAP] and a summary of the user's requirements."
            )
        }
        return [system_prompt] + self.history

    def _extract_profile(self):
        user_inputs = [msg["content"] for msg in self.history if msg["role"] == "user"]
        return "\n".join(user_inputs)