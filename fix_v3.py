with open('/Users/stephenklein/.openclaw/workspace/paycheck/out2/index.html', 'r') as f:
    content = f.read()

fn_start = "async function sendUSDC(){"
end_marker = "}\n\n\n\nwindo"

start = content.find(fn_start)
end = content.find(end_marker, start)

if start == -1 or end == -1:
    print("ERROR: bounds not found. start:", start, "end:", end)
    # Try alternate end marker
    end = content.find("}\n\nwindo", start)
    print("Alternate end:", end)
    if end == -1:
        exit(1)

print("Found function at", start, "to", end)

new_fn = """async function sendUSDC(){
  const recipient=document.getElementById('p_wallet').value.trim();
  const name=document.getElementById('p_name').value;
  const amount=parseFloat(document.getElementById('p_amount').value);
  const note=document.getElementById('p_note').value||'Paycheck payment';
  if(!amount||amount<=0){toast('Enter a valid amount',1);return}
  const btn=document.getElementById('payBtn');
  btn.disabled=true;btn.textContent='Checking accounts...';
  try{
    const prov=window.phantom?.solana||window.solana;
    const conn=new solanaWeb3.Connection(RPC,'confirmed');
    const senderPk=new solanaWeb3.PublicKey(pk);
    const recipPk=new solanaWeb3.PublicKey(recipient);
    const mintPk=new solanaWeb3.PublicKey(USDC_MINT);
    const tokenProgPk=new solanaWeb3.PublicKey(TOKEN_PROG);
    const memoPk=new solanaWeb3.PublicKey(MEMO_PROG);

    // Get sender actual USDC token account
    const senderAccounts=await conn.getParsedTokenAccountsByOwner(senderPk,{mint:mintPk});
    if(!senderAccounts.value.length){
      toast('You do not have a USDC token account',1);
      btn.disabled=false;btn.textContent='Sign & Send USDC';return;
    }
    const senderATA=new solanaWeb3.PublicKey(senderAccounts.value[0].pubkey.toString());

    // Get recipient actual USDC token account
    const recipAccounts=await conn.getParsedTokenAccountsByOwner(recipPk,{mint:mintPk});
    if(!recipAccounts.value.length){
      toast('Recipient does not have a USDC account. They need to hold USDC first.',1);
      btn.disabled=false;btn.textContent='Sign & Send USDC';return;
    }
    const recipATA=new solanaWeb3.PublicKey(recipAccounts.value[0].pubkey.toString());

    // Build SPL transfer instruction
    const amountRaw=BigInt(Math.round(amount*1e6));
    const transferData=new Uint8Array(9);
    transferData[0]=3;
    let amt=amountRaw;
    for(let i=1;i<9;i++){transferData[i]=Number(amt&BigInt(0xff));amt>>=BigInt(8);}

    const tx=new solanaWeb3.Transaction();
    tx.add(new solanaWeb3.TransactionInstruction({
      keys:[
        {pubkey:senderATA,isSigner:false,isWritable:true},
        {pubkey:recipATA,isSigner:false,isWritable:true},
        {pubkey:senderPk,isSigner:true,isWritable:false},
      ],
      programId:tokenProgPk,
      data:transferData
    }));
    tx.add(new solanaWeb3.TransactionInstruction({
      keys:[{pubkey:senderPk,isSigner:true,isWritable:false}],
      programId:memoPk,
      data:new TextEncoder().encode('paycheck:'+amount+':USDC:'+encodeURIComponent(note))
    }));

    const {blockhash}=await conn.getLatestBlockhash();
    tx.recentBlockhash=blockhash;tx.feePayer=senderPk;
    btn.textContent='Waiting for signature...';
    const {signature}=await prov.signAndSendTransaction(tx);

    document.getElementById('payTxLink').href='https://solscan.io/tx/'+signature;
    document.getElementById('payTxLink').textContent=signature.slice(0,20)+'... View on Solscan';
    document.getElementById('payTx').classList.add('show');
    btn.textContent='Sent!';
    pCount++;document.getElementById('payCount').textContent=pCount;
    document.getElementById('actPanel').style.display='block';
    const row=document.createElement('div');
    row.className='activity-item';
    row.innerHTML='<div style="display:flex;justify-content:space-between"><div><span style="color:#6ee7b7;font-weight:600">'+amount+' USDC</span> to '+name+'</div><a href="https://solscan.io/tx/'+signature+'" target="_blank" style="color:#34d399;font-size:11px;font-family:monospace;text-decoration:none">'+signature.slice(0,8)+'... \u2197</a></div><div style="color:#4b5563;font-size:11px;margin-top:4px">'+new Date().toLocaleTimeString()+'</div>';
    document.getElementById('actList').prepend(row);
    toast('Sent '+amount+' USDC to '+name);fetchBal();
    setTimeout(function(){closeModal('payModal');},2500);
  }catch(e){
    btn.disabled=false;btn.textContent='Sign & Send USDC';
    const m=e.message||'';
    if(m.includes('rejected')||m.includes('User'))toast('Cancelled',1);
    else{toast('Error: '+m.slice(0,100),1);console.error('USDC error:',e);}
  }
}"""

new_content = content[:start] + new_fn + "\n\n\n\n" + content[end + len("}\n\n\n\n"):]

with open('/Users/stephenklein/.openclaw/workspace/paycheck/out2/index.html', 'w') as f:
    f.write(new_content)
print("Done. File size:", len(new_content))
