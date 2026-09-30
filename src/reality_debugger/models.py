from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

ClaimType = Literal["factual_claim", "opinion", "prediction", "emotional_language"]
EvidenceStatus = Literal["verified", "unverified", "refuted", "not_applicable"]
PersuasionSignal = Literal[
    "urgency",
    "fear",
    "authority_appeal",
    "social_proof",
    "repetition",
    "us_vs_them_framing",
]
EvidenceRelation = Literal["supports", "contradicts", "contextualizes"]
SourceType = Literal["primary", "secondary", "unknown"]


@dataclass(frozen=True)
class ProvenanceRecord:
    source_id: str
    source_type: SourceType
    locator: str | None = None
    excerpt_hash: str | None = None


@dataclass(frozen=True)
class EvidenceRecord:
    relation: EvidenceRelation
    provenance: ProvenanceRecord


@dataclass(frozen=True)
class AnalyzedElement:
    claim: str
    type: ClaimType
    evidence_status: EvidenceStatus = "unverified"
    persuasion_signals: list[PersuasionSignal] = field(default_factory=list)
    evidence: list[EvidenceRecord] = field(default_factory=list)
    needs_verification: bool = True
