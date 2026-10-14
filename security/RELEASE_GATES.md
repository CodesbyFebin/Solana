# Production and Signing Gates

- [ ] Verify program IDs and deployed bytecode/upgrade authority from trustworthy evidence.
- [ ] Pin exact instruction data, account ordering, signer and writable privileges.
- [ ] Prove every financial operation checks protocol authorization on its own execution path.
- [ ] Simulate the exact transaction before user review; abort if it mutates.
- [ ] Hash and compare serialized transaction messages before and after signing.
- [ ] Cryptographically verify the expected wallet signature.
- [ ] Fail closed on expired blockhashes and RPC uncertainty.
- [ ] Inspect confirmation errors, transaction meta errors, and finality.
- [ ] Decode transaction instructions correctly for legacy and versioned transactions.
- [ ] Reconcile independently verified program state effects.
- [ ] Keep financial operations disabled until all applicable gates pass.
