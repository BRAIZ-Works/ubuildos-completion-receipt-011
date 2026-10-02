# Recovery from failed v1.0.0

Failed subject SHA-256: `53f9a6005a10a53b2d7f35ac0297c2ba4da3ffc559f05b5fc29ca9d5a7d9d62c`
Failed Fresh-IQA handoff SHA-256: `16d554699a6cc10a2825f3621ea473a66a9b436416533e8a69176f20cb04b314`

Fresh-IQA findings reproduced:
1. LinkedIn post did not conform to the included mandatory v1.3.0 campaign structure.
2. Producer validator false-passed when `PUBLIC_MANIFEST.json` and `SHA256SUMS.txt` were missing.

Safe-Change successor v1.0.1 repairs both recurrence classes. Failed predecessor bytes remain preserved outside this successor.
