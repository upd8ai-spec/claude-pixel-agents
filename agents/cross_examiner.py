from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List

from agents.lawyer_agent import LawyerAgent, Proposal


@dataclass
class CrossExaminationResult:
    attacker: str
    target: str
    weaknesses: List[str]
    questions: List[str]

    def to_dict(self) -> Dict[str, object]:
        return {
            "attacker": self.attacker,
            "target": self.target,
            "weaknesses": self.weaknesses,
            "questions": self.questions,
        }


class CrossExaminer:
    """Coordinates cross-examination assignments among lawyer agents."""

    def run(self, lawyers: List[LawyerAgent], proposals: List[Proposal]) -> List[CrossExaminationResult]:
        results: List[CrossExaminationResult] = []
        for idx, lawyer in enumerate(lawyers):
            target = proposals[(idx + 1) % len(proposals)]
            response = lawyer.cross_examine(target)
            results.append(
                CrossExaminationResult(
                    attacker=response["attacker"],
                    target=response["target"],
                    weaknesses=response["weaknesses"],
                    questions=response["questions"],
                )
            )
        return results
