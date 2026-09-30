# Reality Debugger

**Reality Debugger** is an experimental cognitive firewall for decomposing messages into claims, evidence relationships, provenance, and persuasion signals.

The project does **not** assign a "manipulation score" and does not decide what a person should believe. Its goal is to expose the anatomy of a message so the user can inspect it.

## v0.1.0-contract

The first milestone establishes the data contract and safety invariants before implementing claim extraction.

### Core invariants

1. Persuasion is not equivalent to manipulation.
2. Unverified is not equivalent to false or refuted.
3. Repetition is not independent corroboration.
4. Linguistic analysis cannot independently authorize `verified` or `refuted`.
5. Evidence verdicts require provenance.
6. The final judgment remains with the human.

## Pipeline

```text
Input
  -> Preprocessor
  -> Claim Extractor
  -> Persuasion Analyzer
  -> Evidence Mapper
  -> Evidence Resolver
  -> Reality Debugger Output
  -> Human judgment
```

## Development

```bash
python -m pip install -e ".[dev]"
pytest
```

## Status

Early experimental research software. The current milestone defines contracts and invariants; it is not a fact-checker or production moderation system.
