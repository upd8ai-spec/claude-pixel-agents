# Courtroom Multi-Agent Debate System

This repository now provides a **courtroom-style multi-agent debate simulator**.

## Roles

- **Lawyer Agents**: generate proposals, critique opponents, and defend their own architecture.
- **Jury Agents**: score each proposal against objective criteria and vote.
- **Bailiff (Orchestrator)**: runs rounds, routes arguments, collects scores, and announces verdict.

## Courtroom Workflow

1. `round_1_generate_proposals()`
2. `round_2_cross_examination()`
3. `round_3_defense()`
4. `round_4_jury_scoring()`
5. `round_5_final_verdict()`

## Project Structure

```
agents/
  lawyer_agent.py
  jury_agent.py
  cross_examiner.py
orchestrator/
  courtroom_orchestrator.py
prompts/
  lawyer_prompt.txt
  jury_prompt.txt
  cross_exam_prompt.txt
workflows/
  debate_workflow.py
main.py
```

## Run End-to-End Simulation

```bash
python main.py
```

Use custom settings:

```bash
python main.py "Design an AI PMO system using Python and Supabase" --lawyers 4 --jury 5 --transcript courtroom_transcript.log
```

## Output Format

The simulation prints:

- `CASE`
- `LAWYER PROPOSALS`
- `CROSS EXAMINATION`
- `DEFENSE RESPONSES`
- `JURY SCORES`
- `FINAL VERDICT`

## Extra Features Included

- Configurable number of lawyer agents (`--lawyers`)
- Configurable number of jury members (`--jury`)
- Debate memory across rounds in orchestrator state
- ASCII scoring visualization
- Transcript logging to file
