# Solana — CodesbyFebin

A curated Solana development workspace for programs, wallets, transactions, RPC, mobile integration, examples, and production security qualification. **Reference catalog only: not a merged fork or deployed protocol.**

## Navigation

- [Source catalog](catalog/repos.json): 47 repositories in nine categories
- [Reference directory](docs/REFERENCE_CATALOG.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Development workflow](docs/DEVELOPMENT.md)
- [Ecosystem partners](docs/PARTNERS.md)
- [Release gates](security/RELEASE_GATES.md)
- [Read-only RPC sample](examples/read-only-rpc/read-account.mjs)

## Principles

Use maintained canonical libraries when appropriate; retain upstream licenses and exact commit revisions. Fetch only needed upstream code into ignored vendor directories. Never expose wallet secrets or infer instruction layouts. Transaction signing requires immutable message review and byte-exact signing, simulation, signature verification, execution error inspection and protocol-specific reconciliation.

Clone references with `python3 scripts/fetch_sources.py --groups solana-developers solana-program`. Verify the catalogue with `python3 scripts/validate_catalog.py`.

Separate project: [ORE-Minecraft](https://github.com/CodesbyFebin/ORE-Minecraft). Official documentation: https://solana.com/docs.
