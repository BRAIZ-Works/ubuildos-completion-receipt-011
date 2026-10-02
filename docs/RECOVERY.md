# Recovery
The release is file-based. Recovery target: the exact frozen release ZIP after owner acceptance. Restore by replacing the public projection with the frozen file set and verifying SHA256SUMS plus the manifest. Until freeze/deployment occurs, recovery status is candidate-only; no live rollback claim is made.
