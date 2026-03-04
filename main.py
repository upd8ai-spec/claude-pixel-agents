from __future__ import annotations

import argparse

from orchestrator.courtroom_orchestrator import CourtroomConfig
from workflows.debate_workflow import CourtroomDebateWorkflow, format_debate_output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Courtroom multi-agent debate simulator")
    parser.add_argument(
        "case",
        nargs="?",
        default="Design an AI PMO system using Python and Supabase",
        help="Problem statement to debate",
    )
    parser.add_argument("--lawyers", type=int, default=3, help="Number of lawyer agents")
    parser.add_argument("--jury", type=int, default=3, help="Number of jury agents")
    parser.add_argument(
        "--transcript",
        default="courtroom_transcript.log",
        help="Path to transcript log",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = CourtroomConfig(num_lawyers=args.lawyers, num_jury=args.jury, transcript_log_path=args.transcript)
    workflow = CourtroomDebateWorkflow(config)
    result = workflow.run(args.case)
    print(format_debate_output(result))


if __name__ == "__main__":
    main()
