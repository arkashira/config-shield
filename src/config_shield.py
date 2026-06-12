import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Alert:
    text_snippet: str
    config_profile_id: str

class ConfigShield:
    def __init__(self, threshold: float = 0.8, max_latency: float = 200):
        self.threshold = threshold
        self.max_latency = max_latency

    def detect(self, response: str, confidence: Dict[str, float]) -> Alert:
        if confidence['hallucination'] > self.threshold or confidence['toxicity'] > self.threshold:
            return Alert(text_snippet=response, config_profile_id='default')

    def send_alert(self, alert: Alert):
        # Simulate sending alert via webhook and UI notification
        print(f"Alert: {alert.text_snippet} (Config Profile ID: {alert.config_profile_id})")

def main():
    config_shield = ConfigShield()
    response = "This is a test response."
    confidence = {'hallucination': 0.9, 'toxicity': 0.1}
    alert = config_shield.detect(response, confidence)
    if alert:
        config_shield.send_alert(alert)

if __name__ == "__main__":
    main()
