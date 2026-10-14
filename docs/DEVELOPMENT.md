# Development Workflow

1. Install supported Rust, Solana CLI, Anchor and JavaScript toolchains from https://solana.com/docs.
2. Read source licenses and select only the dependencies relevant to the feature.
3. Run `python3 scripts/validate_catalog.py`.
4. Use `python3 scripts/fetch_sources.py --groups solana-program` for optional local snapshots.
5. Build and test against local SVM runtimes or a local validator before devnet integration.
6. Test wallets on physical devices before enabling mainnet flows.
7. Complete all release gates in `security/RELEASE_GATES.md`.
