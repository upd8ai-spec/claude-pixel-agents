from __future__ import annotations

from dataclasses import dataclass
from statistics import mean
from typing import Dict, List

from agents.lawyer_agent import Proposal

CRITERIA = ["feasibility", "simplicity", "scalability", "cost", "speed_to_build"]


@dataclass
class JuryEvaluation:
    jury_name: str
    proposal_agent: str
    scores: Dict[str, int]
    reasoning: str

    @property
    def total(self) -> float:
        return mean(self.scores.values())


class JuryAgent:
    """Jury member that scores each proposal and casts a vote."""

    def __init__(self, name: str, strictness: int = 0) -> None:
        self.name = name
        self.strictness = strictness

    def evaluate_proposal(self, proposal: Proposal) -> JuryEvaluation:
        base = {
            "Monolith First": {"feasibility": 9, "simplicity": 9, "scalability": 6, "cost": 8, "speed_to_build": 9},
            "Event-Driven": {"feasibility": 7, "simplicity": 5, "scalability": 9, "cost": 6, "speed_to_build": 5},
            "Serverless Lean": {"feasibility": 8, "simplicity": 7, "scalability": 8, "cost": 7, "speed_to_build": 8},
        }

        if "message bus" in proposal.architecture:
            strategy = "Event-Driven"
        elif "Edge Functions" in proposal.architecture:
            strategy = "Serverless Lean"
        else:
            strategy = "Monolith First"

        adjusted = {k: max(1, min(10, v - self.strictness)) for k, v in base[strategy].items()}
        reasoning = (
            f"{self.name} finds {proposal.agent_name}'s proposal {strategy} with strengths in "
            f"{', '.join(sorted(adjusted, key=adjusted.get, reverse=True)[:2])}."
        )
        return JuryEvaluation(self.name, proposal.agent_name, adjusted, reasoning)

    def vote(self, evaluations: List[JuryEvaluation]) -> str:
        best = max(evaluations, key=lambda x: x.total)
        return best.proposal_agent
