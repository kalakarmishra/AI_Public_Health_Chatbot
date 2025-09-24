from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionFetchVaccination(Action):
    def name(self) -> str:
        return "action_fetch_vaccination"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        # Dummy API (replace with real one later)
        try:
            response = requests.get("https://mocki.io/v1/0c63dc37-9c15-42a7-a8f7-9c7e21d8c223")  
            data = response.json()
            message = "📅 Vaccination Schedule:\n"
            for v in data["vaccines"][:3]:
                message += f"- {v['name']} at age {v['age']} months\n"
        except Exception as e:
            message = "⚠️ Sorry, I couldn’t fetch vaccination info right now. Please check your local health center."

        dispatcher.utter_message(text=message)
        return []


class ActionFetchOutbreakData(Action):
    def name(self) -> str:
        return "action_fetch_outbreak_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        # Dummy API (replace with real one later)
        try:
            response = requests.get("https://mocki.io/v1/96ddc1a0-0a91-4c8e-8a14-bb1e77a9c45b")
            data = response.json()
            message = "🚨 Current Outbreaks:\n"
            for o in data["outbreaks"]:
                message += f"- {o['disease']} in {o['location']} ({o['cases']} cases)\n"
        except Exception as e:
            message = "⚠️ Sorry, outbreak info is currently unavailable."

        dispatcher.utter_message(text=message)
        return []

class ActionFetchSymptoms(Action):
    def name(self) -> str:
        return "action_fetch_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        message = (
            "🩺 Common symptoms of viral infections include:\n"
            "- Fever\n"
            "- Cough\n"
            "- Fatigue\n"
            "- Body ache\n\n"
            "👉 Please consult a doctor for an accurate diagnosis."
        )
        dispatcher.utter_message(text=message)
        return []

