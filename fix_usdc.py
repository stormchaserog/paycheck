with open('/Users/stephenklein/.openclaw/workspace/paycheck/out2/index.html', 'r') as f:
    content = f.read()

old_fn_start = "async function sendUSDC(){"
start_idx = content.find(old_fn_start)
end_idx = content.find("}\n\nwindow.addEventListener('load'", start_idx)

if start_idx == -1 or end_idx == -1:
    print("Could not find function bounds. start:", start_idx, "end:", end_idx)
    exit(1)

new_fn = """async function sendUSDC(){
  const recipient=document.getElementById('p_wallet').value.trim();
  const name=document.getElementById('p_name').value;
  const amount=parseFloat(document.getElementById('p_amount').value);
  const note=document.getElementById('p_note').value||'Paycheck payment';
  if(!amount||amount<=0){toast('Enter a valid amount',1);return}
  const btn=document.getElementById('payBtn');
  btn.disabled=true;btn.textContent='Building transaction...';
  try{
    const prov=window.phantom?.solana||window.solana;
    const conn=new solanaWeb3.Connection(RPC,'confirmed');
    const senderPk=new solanaWeb3.PublicKey(pk);
    const recipPk=new solanaWeb3.PublicKey(recipient);
    const tokenProgPk=new solanaWeb3.PublicKey(TOKEN_PROG);
    const memoPk=new solanaWeb3.PublicKey(MEMO_PROG);
    const mintPk=new solanaWeb3.PublicKey(USDC_MINT);
    const assocProgPk=new solanaWeb3.PublicKey(ASSOC_PROG);
    const sysvarRent=new solanaWeb3.PublicKey('SysvarRent111111111111111111111111111111111');

    const senderATA=await getATA(pk,USDC_MINT);
    const recipATA=await getATA(recipient,USDC_MINT);

    const tx=new solanaWeb3.Transaction();

    const recipATAInfo=await conn.getAccountInfo(recipATA);
    if(!recipATAInfo){
      tx.add(new solanaWeb3.TransactionInstruction({
        keys:[
          {pubkey:senderPk,isSigner:true,isWritable:true},
          {pubkey:recipATA,isSigner:false,isWritable:true},
          {pubkey:recipPk,isSigner:false,isWritable:false},
          {pubkey:mintPk,isSigner:false,isWritable:false},
          {pubkey:solanaWeb3.SystemProgram.programId,isSigner:false,isWritable:false},
          {pubkey:tokenProgPk,isSigner:false,isWritable:false},
          {pubkey:sysvarRent,isSigner:false,isWritable:false},
        ],
        programId:assocProgPk,
        data:new Uint8Array(0)
      }));
    }

    const amountRaw=BigInt(Math.round(amount*1e6));
    const transferData=new Uint8Array(9);
    transferData[0]=3;
    let amt=amountRaw;
    for(let i=1;i<9;i++){transferData[i]=Number(amt&BigInt(0xff));amt>>=BigInt(8);}

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
    row.innerHTML='<div style="display:flex;justify-content:space-between"><div><span style="color:#6ee7b7;font-weight:600">'+amount+' USDC</span> to '+name+'</div><a href="https://solscan.io/tx/'+signature+'" target="_blank" style="color:#34d399;font-size:11px;font-family:monospace;text-decoration:none">'+signature.slice(0,8)+'... &#8599;</a></div><div style="color:#4b5563;font-size:11px;margin-top:4px">'+new Date().toLocaleTimeString()+'</div>';
    document.getElementById('actList').prepend(row);
    toast('Sent '+amount+' USDC to '+name);fetchBal();
  }catch(e){
    btn.disabled=false;btn.textContent='Sign & Send USDC';
    const m=e.message||'';
    if(m.includes('rejected')||m.includes('User'))toast('Cancelled',1);
    else{toast('Error: '+m.slice(0,100),1);console.error(e);}
  }
}
"""

new_content = content[:start_idx] + new_fn + "\n" + content[end_idx + 1:]

with open('/Users/stephenklein/.openclaw/workspace/paycheck/out2/index.html', 'w') as f:
    f.write(new_content)

print("Done. File size:", len(new_content))
