with open('/Users/stephenklein/.openclaw/workspace/paycheck/out2/index.html', 'r') as f:
    content = f.read()

# Fix 1: ATA creation - use create_idempotent (byte [1]) instead of create (byte [0] = empty)
old_ata = "        data:new Uint8Array(0)"
new_ata = "        data:new Uint8Array([1])"
if old_ata in content:
    content = content.replace(old_ata, new_ata)
    print("Fix 1: ATA create_idempotent applied")
else:
    print("Fix 1: ATA instruction not found - checking...")
    idx = content.find("ASSOC_PROG")
    print("ASSOC_PROG found at:", idx)

# Fix 2: Close modal after success + reset button
old_success = "    toast('Sent '+amount+' USDC to '+name);fetchBal();"
new_success = """    toast('Sent '+amount+' USDC to '+name);fetchBal();
    setTimeout(function(){closeModal('payModal');},2000);"""
if old_success in content:
    content = content.replace(old_success, new_success)
    print("Fix 2: Modal auto-close applied")
else:
    print("Fix 2: success line not found")

# Fix 3: Pre-populate example contributor on first load if storage is empty
old_load = "window.addEventListener('load',async()=>{"
new_load = """window.addEventListener('load',async()=>{
  // Seed example contributor if storage is empty
  if(contribs.length===0){
    contribs=[{n:'Example Contributor',w:'F36xnoonUg9rojAyie4WDVSeDCPjwraM1W9vRZgpMzwY',r:'2000'}];
    localStorage.setItem('pc_c',JSON.stringify(contribs));
  }"""
if old_load in content:
    content = content.replace(old_load, new_load)
    print("Fix 3: Example contributor seed applied")
else:
    print("Fix 3: load event not found")

with open('/Users/stephenklein/.openclaw/workspace/paycheck/out2/index.html', 'w') as f:
    f.write(content)
print("Done. File size:", len(content))
