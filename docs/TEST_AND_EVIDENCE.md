# Test and Evidence Model

## Frozen product verification

The exact v1.0.1 product subject passed producer QA and Fresh Independent IQA.

Fresh IQA independently verified:
- exact subject identity;
- archive/path safety;
- governed population and manifest agreement;
- SHA256SUMS replay;
- four required workflow states;
- synthetic/no-external-runtime boundary;
- publication-gate behavior;
- LinkedIn v1.3.0 structure;
- predecessor failure-family closure.

## Preserved failure families

### v1.0.0 family 1 — campaign-standard nonconformance
The LinkedIn draft did not satisfy the included byte-locked Day-10 campaign standard. v1.0.1 repaired the required structure and added mechanical checks.

### v1.0.0 family 2 — integrity-oracle false PASS
The original producer verifier could still return PASS after required integrity files were removed. The successor fail-closes on missing manifest/checksum indexes and related population/hash drift.

## Mutation controls

The successor producer package included eight adversarial mutations intended to prove the verifier rejects unsafe or semantically weakened variants.

## Public projection verification

The public projection is checked separately from the frozen product subject. Public-projection verification covers required documentation population, names/versions/status, live/repository link consistency, public-only content boundaries, manifest/checksum agreement, and false lifecycle advancement.

A public-projection PASS does not alter the frozen product SHA-256 or become a new Fresh-IQA result.
