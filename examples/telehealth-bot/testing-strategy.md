# Testing Strategy – Telehealth Triage Bot

## Clinical Validation (Golden Set)
- **Dataset**: 500 anonymized historical triage cases (Expert labeled).
- **Pass Criteria**: AI must match Expert label > 95% of the time.
- **Critical Failure**: AI **under-triaging** a life-threatening condition (Severity 1 classified as Severity 3+). FAILURE = BLOCK RELEASE.

## Automated Tests
- **Unit**: Component logic (Router, Gateway, Encryption utils).
- **Integration**: Gateway <-> AI Service (latency & error handling).
- **E2E**: Full chat flow simulation (Mocked AI for determinism).

## Security Testing
- **Static Analysis**: SAST tools in CI/CD.
- **Dynamic Analysis**: DAST scans on staging.
- **Pen-testing**: Regular manual penetration tests.

## Release Gate
- Zero Critical/High vulnerabilities.
- >95% Clinical Accuracy.
- Compliance sign-off on Audit Logs.
