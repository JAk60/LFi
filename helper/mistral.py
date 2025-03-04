import ollama
from typing import Dict, Any
import time
import re


class SentenceExtractor:
    def __init__(self, model: str = "mistral"):
        self.model = model
        self.extracted_data = {}


class SentenceExtractor:
    def __init__(self, model: str = "mistral"):
        self.model = model
        self.extracted_data = {}

    def extract(self, sentence: str) -> Dict[str, Any]:
        """Extract information including naval distances from sentence."""
        prompt = (
            """Extract time, location, action, and operational range/distance from this sentence. For naval contexts, distances are in nautical miles (nm). Return only these elements:"""
            + f"\n{sentence}"
        )

        for attempt in range(3):
            try:
                response = ollama.generate(
                    model=self.model,
                    prompt=prompt,
                    stream=False,
                    options={"temperature": 0.1, "top_p": 0.95},
                )

                parsed_response = response["response"].strip()

                for line in parsed_response.split("\n"):
                    if "time:" in line.lower():
                        self.extracted_data["time"] = line.split(":", 1)[1].strip()
                    elif "location:" in line.lower():
                        self.extracted_data["location"] = line.split(":", 1)[1].strip()
                    elif "action:" in line.lower():
                        self.extracted_data["action"] = line.split(":", 1)[1].strip()
                    elif any(x in line.lower() for x in ["range:", "distance:"]):
                        self.extracted_data["distance"] = self._extract_distance(
                            line.split(":", 1)[1].strip()
                        )

                if "distance" not in self.extracted_data:
                    distance_match = re.search(
                        r"(\d+(?:\.\d+)?)\s*(?:nautical miles?|nm|nmi)",
                        sentence,
                        re.IGNORECASE,
                    )
                    if distance_match:
                        self.extracted_data["distance"] = float(distance_match.group(1))

                return self.extracted_data

            except Exception as e:
                if attempt == 2:
                    raise RuntimeError(f"Failed to process: {str(e)}")
                time.sleep(2)

    def _extract_distance(self, distance_str: str) -> float:
        """Extract and return distance as float value in nautical miles."""
        nm_match = re.search(
            r"(\d+(?:\.\d+)?)\s*(?:nautical miles?|nm|nmi)", distance_str, re.IGNORECASE
        )
        if nm_match:
            return float(nm_match.group(1))

        num_match = re.search(r"(\d+(?:\.\d+)?)", distance_str)
        return float(num_match.group(1)) if num_match else 0.0

    def apply_rule(self, rule: str, text: str) -> bool:
        """
        Check if a given rule applies to the text using Mistral.

        Args:
            rule (str): The rule to check
            text (str): The text to evaluate against the rule

        Returns:
            bool: True if the rule applies, False otherwise
        """
        prompt = f"""Determine if the following rule applies to the given text:

        Rule: {rule}
        Text: {text}

        Respond with only YES or NO."""

        for attempt in range(3):
            try:
                response = ollama.generate(
                    model=self.model,
                    prompt=prompt,
                    stream=False,
                    options={"temperature": 0.1, "top_p": 0.95},
                )

                cleaned_response = response["response"].strip().lower()

                return cleaned_response == "yes"

            except Exception as e:
                if attempt == 2:
                    raise RuntimeError(f"Failed to process rule check: {str(e)}")
                time.sleep(2)

        return False

    def get_time(self) -> str:
        return self.extracted_data.get("time", "")

    def get_location(self) -> str:
        return self.extracted_data.get("location", "")

    def get_action(self) -> str:
        return self.extracted_data.get("action", "")

    def get_distance(self) -> float:
        return self.extracted_data.get("distance", 0.0)

    def get_all(self) -> Dict[str, Any]:
        return self.extracted_data

    def get_time(self) -> str:
        return self.extracted_data.get("time", "")

    def get_location(self) -> str:
        return self.extracted_data.get("location", "")

    def get_action(self) -> str:
        return self.extracted_data.get("action", "")

    def get_distance(self) -> str:
        return self.extracted_data.get("distance", "")

    def get_all(self) -> Dict[str, str]:
        return self.extracted_data
