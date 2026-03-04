from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Proposal:
    agent_name: str
    architecture: str
    reasoning: str
    tradeoffs: str
    assumptions: str

    def as_dict(self) -> Dict[str, str]:
        return {
            "agent_name": self.agent_name,
            "architecture": self.architecture,
            "reasoning": self.reasoning,
            "tradeoffs": self.tradeoffs,
            "assumptions": self.assumptions,
        }


class LawyerAgent:
    """Lawyer agent that proposes, attacks competitors, and defends its case."""

    STRATEGIES = [
        {
            "name": "Monolith First",
            "architecture": "Python FastAPI monolith + Supabase Postgres + background jobs (Celery/Redis) + lightweight React UI.",
            "reasoning": "Fast delivery with low coordination overhead and a single deployable backend.",
            "tradeoffs": "Less independent scaling by service and tighter coupling as scope grows.",
            "assumptions": "Team is small, requirements are still evolving, and delivery speed is critical.",
        },
        {
            "name": "Event-Driven",
            "architecture": "Python services over message bus, Supabase Postgres for state, async workers for automations, and API gateway.",
            "reasoning": "Improves scalability and fault isolation for heavy workloads and workflow orchestration.",
            "tradeoffs": "Higher complexity, more observability needs, and slower initial setup.",
            "assumptions": "System must handle varied workloads and long-running asynchronous processes.",
        },
        {
            "name": "Serverless Lean",
            "architecture": "Supabase Edge Functions + Python micro APIs + managed queues + template-driven workflow engine.",
            "reasoning": "Minimizes ops burden and accelerates time-to-market with managed infrastructure.",
            "tradeoffs": "Potential vendor lock-in and less control over lower-level optimization.",
            "assumptions": "Traffic pattern is bursty and cost optimization at low-to-medium scale matters.",
        },
    ]

    def __init__(self, name: str, style_index: int = 0) -> None:
        self.name = name
        self.style = self.STRATEGIES[style_index % len(self.STRATEGIES)]

    def generate_proposal(self, case: str) -> Proposal:
        return Proposal(
            agent_name=self.name,
            architecture=f"{self.style['architecture']} Case fit: {case}.",
            reasoning=self.style["reasoning"],
            tradeoffs=self.style["tradeoffs"],
            assumptions=self.style["assumptions"],
        )

    def cross_examine(self, other_proposal: Proposal) -> Dict[str, List[str]]:
        claims = [
            f"Scalability challenge: How does {other_proposal.agent_name} avoid bottlenecks during peak throughput?",
            f"Cost challenge: Which components in {other_proposal.agent_name}'s architecture are most likely to exceed budget?",
            "Security challenge: Where are auth boundaries, secrets management, and audit trails enforced?",
            "Complexity challenge: Which subsystem is hardest to operate and why is that complexity justified?",
            "Assumption challenge: Which assumption is least validated by user demand or implementation constraints?",
        ]
        weaknesses = [
            "Potential underestimation of integration overhead.",
            "May not include enough resilience detail for production incidents.",
            "Tradeoff narrative could downplay long-term maintenance burden.",
        ]
        return {"attacker": self.name, "target": other_proposal.agent_name, "weaknesses": weaknesses, "questions": claims}

    def defend(self, criticisms: List[Dict[str, List[str]]], proposal: Proposal) -> str:
        points = [f"{self.name} Defense:", "- Our design intentionally prioritizes practical delivery constraints."]
        for critique in criticisms:
            points.append(
                f"- Response to {critique['attacker']}: We address risk via staged rollouts, explicit SLOs, and telemetry-driven tuning."
            )
        points.append(f"- Architecture remains: {proposal.architecture}")
        points.append("- We accept known tradeoffs and include migration pathways as complexity grows.")
        return "\n".join(points)
