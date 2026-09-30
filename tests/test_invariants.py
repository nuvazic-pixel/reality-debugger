from reality_debugger.models import AnalyzedElement, EvidenceRecord, ProvenanceRecord


def test_unverified_does_not_mean_refuted():
    element = AnalyzedElement(
        claim="The city announced construction will begin Tuesday.",
        type="factual_claim",
    )
    assert element.evidence_status == "unverified"
    assert element.evidence_status != "refuted"


def test_persuasion_does_not_imply_falsehood():
    element = AnalyzedElement(
        claim="We must reduce costs before winter.",
        type="prediction",
        persuasion_signals=["urgency"],
    )
    assert element.persuasion_signals == ["urgency"]
    assert element.evidence_status != "refuted"


def test_emotional_language_can_be_not_applicable_for_evidence():
    element = AnalyzedElement(
        claim="This is outrageous!",
        type="emotional_language",
        evidence_status="not_applicable",
        needs_verification=False,
    )
    assert element.evidence_status == "not_applicable"
    assert element.needs_verification is False


def test_factual_claim_without_evidence_remains_unverified():
    element = AnalyzedElement(
        claim="The project will cost twelve million euros.",
        type="factual_claim",
    )
    assert element.evidence == []
    assert element.evidence_status == "unverified"
    assert element.needs_verification is True


def test_multiple_persuasion_signals_do_not_create_truth_verdict():
    element = AnalyzedElement(
        claim="Act now before it is too late.",
        type="emotional_language",
        evidence_status="not_applicable",
        persuasion_signals=["urgency", "fear", "us_vs_them_framing"],
        needs_verification=False,
    )
    assert len(element.persuasion_signals) == 3
    assert element.evidence_status == "not_applicable"


def test_evidence_has_explicit_provenance():
    provenance = ProvenanceRecord(
        source_id="source-A",
        source_type="primary",
        locator="https://example.invalid/document",
        excerpt_hash="sha256:abc123",
    )
    evidence = EvidenceRecord(relation="supports", provenance=provenance)

    assert evidence.provenance.source_id == "source-A"
    assert evidence.relation == "supports"


def test_llm_cannot_authorize_evidence_verdict():
    llm_allowed_statuses = {"unverified", "not_applicable"}
    assert "verified" not in llm_allowed_statuses
    assert "refuted" not in llm_allowed_statuses
