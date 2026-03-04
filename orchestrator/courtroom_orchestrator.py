from __future__ import annotations

from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from statistics import mean
from typing import Dict, List

from agents.cross_examiner import CrossExaminer, CrossExaminationResult
from agents.jury_agent import CRITERIA, JuryAgent, JuryEvaluation
from agents.lawyer_agent import LawyerAgent, Proposal


@dataclass
class CourtroomConfig:
    num_lawyers: int = 3
    num_jury: int = 3
    transcript_log_path: str = "courtroom_transcript.log"


@dataclass
class DebateMemory:
    proposals: List[Proposal] = field(default_factory=list)
    cross_examinations: List[CrossExaminationResult] = field(default_factory=list)
    defenses: Dict[str, str] = field(default_factory=dict)
    jury_scores: Dict[str, List[JuryEvaluation]] = field(default_factory=lambda: defaultdict(list))
    jury_votes: List[str] = field(default_factory=list)


class CourtroomOrchestrator:
    """Bailiff orchestration for courtroom debate rounds."""

    def __init__(self, config: CourtroomConfig) -> None:
        self.config = config
        self.memory = DebateMemory()
        self.lawyers = [LawyerAgent(name=f"Lawyer Agent {chr(65 + i)}", style_index=i) for i in range(config.num_lawyers)]
        self.jury = [JuryAgent(name=f"Jury Agent {i + 1}", strictness=i % 2) for i in range(config.num_jury)]
        self.cross_examiner = CrossExaminer()

    def round_1_generate_proposals(self, case: str) -> List[Proposal]:
        self.memory.proposals = [lawyer.generate_proposal(case) for lawyer in self.lawyers]
        self._log("ROUND 1", f"Generated {len(self.memory.proposals)} proposals")
        return self.memory.proposals

    def round_2_cross_examination(self) -> List[CrossExaminationResult]:
        self.memory.cross_examinations = self.cross_examiner.run(self.lawyers, self.memory.proposals)
        self._log("ROUND 2", f"Completed {len(self.memory.cross_examinations)} cross examinations")
        return self.memory.cross_examinations

    def round_3_defense(self) -> Dict[str, str]:
        grouped: Dict[str, List[Dict[str, List[str]]]] = defaultdict(list)
        for item in self.memory.cross_examinations:
            grouped[item.target].append(item.to_dict())

        self.memory.defenses = {}
        for proposal in self.memory.proposals:
            lawyer = next(l for l in self.lawyers if l.name == proposal.agent_name)
            self.memory.defenses[proposal.agent_name] = lawyer.defend(grouped[proposal.agent_name], proposal)

        self._log("ROUND 3", "Defense statements recorded")
        return self.memory.defenses

    def round_4_jury_scoring(self) -> Dict[str, Dict[str, float]]:
        self.memory.jury_scores = defaultdict(list)
        for juror in self.jury:
            for proposal in self.memory.proposals:
                evaluation = juror.evaluate_proposal(proposal)
                self.memory.jury_scores[proposal.agent_name].append(evaluation)

        summary: Dict[str, Dict[str, float]] = {}
        for proposal_agent, evaluations in self.memory.jury_scores.items():
            per_criteria = {c: mean(e.scores[c] for e in evaluations) for c in CRITERIA}
            summary[proposal_agent] = {**per_criteria, "average": mean(per_criteria.values())}

        self._log("ROUND 4", "Jury scoring complete")
        return summary

    def round_5_final_verdict(self) -> Dict[str, object]:
        votes: List[str] = []
        for juror in self.jury:
            juror_evals = [
                e
                for proposal_evals in self.memory.jury_scores.values()
                for e in proposal_evals
                if e.jury_name == juror.name
            ]
            votes.append(juror.vote(juror_evals))

        self.memory.jury_votes = votes
        tally = Counter(votes)
        winner = tally.most_common(1)[0][0]
        self._log("ROUND 5", f"Final verdict winner: {winner}")
        return {"winner": winner, "vote_tally": dict(tally)}

    def scoring_visualization(self, score_summary: Dict[str, Dict[str, float]]) -> str:
        lines = ["JURY SCOREBOARD"]
        for agent, metrics in sorted(score_summary.items(), key=lambda item: item[1]["average"], reverse=True):
            bar = "█" * int(round(metrics["average"]))
            lines.append(f"- {agent:15} {metrics['average']:.2f} {bar}")
        return "\n".join(lines)

    def _log(self, stage: str, message: str) -> None:
        stamp = datetime.utcnow().isoformat(timespec="seconds")
        Path(self.config.transcript_log_path).write_text("", encoding="utf-8") if not Path(self.config.transcript_log_path).exists() else None
        with Path(self.config.transcript_log_path).open("a", encoding="utf-8") as fh:
            fh.write(f"[{stamp}] {stage}: {message}\n")
