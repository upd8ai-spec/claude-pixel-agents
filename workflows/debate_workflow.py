from __future__ import annotations

from typing import Dict

from orchestrator.courtroom_orchestrator import CourtroomConfig, CourtroomOrchestrator


class CourtroomDebateWorkflow:
    def __init__(self, config: CourtroomConfig | None = None) -> None:
        self.orchestrator = CourtroomOrchestrator(config or CourtroomConfig())

    def run(self, case: str) -> Dict[str, object]:
        proposals = self.orchestrator.round_1_generate_proposals(case)
        cross_exams = self.orchestrator.round_2_cross_examination()
        defenses = self.orchestrator.round_3_defense()
        score_summary = self.orchestrator.round_4_jury_scoring()
        verdict = self.orchestrator.round_5_final_verdict()

        return {
            "case": case,
            "proposals": proposals,
            "cross_examinations": cross_exams,
            "defenses": defenses,
            "jury_score_summary": score_summary,
            "jury_scoreboard": self.orchestrator.scoring_visualization(score_summary),
            "verdict": verdict,
        }


def format_debate_output(result: Dict[str, object]) -> str:
    lines: list[str] = []
    lines.append("CASE:")
    lines.append(str(result["case"]))
    lines.append("\nLAWYER PROPOSALS")

    for proposal in result["proposals"]:
        lines.append(f"\n{proposal.agent_name}")
        lines.append(f"- architecture: {proposal.architecture}")
        lines.append(f"- reasoning: {proposal.reasoning}")
        lines.append(f"- tradeoffs: {proposal.tradeoffs}")
        lines.append(f"- assumptions: {proposal.assumptions}")

    lines.append("\nCROSS EXAMINATION")
    for item in result["cross_examinations"]:
        lines.append(f"\n{item.attacker} critiques {item.target}")
        lines.extend([f"- weakness: {w}" for w in item.weaknesses])
        lines.extend([f"- question: {q}" for q in item.questions])

    lines.append("\nDEFENSE RESPONSES")
    for agent, response in result["defenses"].items():
        lines.append(f"\n{agent}")
        lines.append(response)

    lines.append("\nJURY SCORES")
    for agent, summary in result["jury_score_summary"].items():
        lines.append(f"\n{agent}")
        for key, value in summary.items():
            lines.append(f"- {key}: {value:.2f}")

    lines.append("\n" + result["jury_scoreboard"])
    lines.append("\nFINAL VERDICT")
    lines.append(f"Winner: {result['verdict']['winner']}")
    lines.append(f"Vote tally: {result['verdict']['vote_tally']}")
    return "\n".join(lines)
