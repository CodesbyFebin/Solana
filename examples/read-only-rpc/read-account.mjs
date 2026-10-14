// Read-only public RPC demo. No wallet or signing.
const endpoint=process.env.SOLANA_RPC_URL || 'https://api.devnet.solana.com';
const pubkey=process.argv[2];
if(!pubkey || !/^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(pubkey)) {
  console.error('Usage: node read-account.mjs <base58-public-key>'); process.exit(2);
}
const res=await fetch(endpoint,{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({jsonrpc:'2.0',id:1,method:'getAccountInfo',params:[pubkey,{encoding:'base64',commitment:'confirmed'}]})});
if(!res.ok)throw Error('HTTP '+res.status);
const body=await res.json();if(body.error)throw Error(JSON.stringify(body.error));
console.log(JSON.stringify({slot:body.result.context.slot,owner:body.result.value?.owner??null,lamports:body.result.value?.lamports??null},null,2));
