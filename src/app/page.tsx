export default function Home() {
  return (
    <main style={{minHeight:'100vh',background:'#000',color:'#fff',fontFamily:'Inter,system-ui,sans-serif'}}>
      {/* Hero */}
      <section style={{display:'flex',flexDirection:'column',alignItems:'center',justifyContent:'center',minHeight:'100vh',padding:'0 24px',textAlign:'center'}}>
        <div style={{maxWidth:'720px',margin:'0 auto'}}>
          <p style={{fontSize:'12px',letterSpacing:'0.2em',textTransform:'uppercase',color:'#9ca3af',marginBottom:'24px'}}>
            White Claw — Crypto-Native Fintech
          </p>
          <h1 style={{fontSize:'clamp(48px,8vw,80px)',fontWeight:'700',letterSpacing:'-0.02em',marginBottom:'24px',lineHeight:'1.1'}}>
            Paycheck
          </h1>
          <p style={{fontSize:'clamp(18px,2.5vw,22px)',color:'#d1d5db',marginBottom:'16px',lineHeight:'1.6'}}>
            Stablecoin payroll with yield-powered advances for crypto-native teams.
          </p>
          <p style={{color:'#6b7280',marginBottom:'48px',maxWidth:'520px',margin:'0 auto 48px',lineHeight:'1.7'}}>
            Set up your team once. Funds earn yield automatically. Contributors get paid on schedule — and can advance their next paycheck instantly at zero cost.
          </p>
          <div style={{display:'flex',gap:'16px',justifyContent:'center',flexWrap:'wrap'}}>
            <button style={{background:'#fff',color:'#000',fontWeight:'600',padding:'16px 32px',borderRadius:'8px',border:'none',cursor:'pointer',fontSize:'16px'}}>
              Get Early Access
            </button>
            <button style={{background:'transparent',color:'#fff',fontWeight:'600',padding:'16px 32px',borderRadius:'8px',border:'1px solid #374151',cursor:'pointer',fontSize:'16px'}}>
              Watch Demo
            </button>
          </div>
        </div>
      </section>

      {/* How it works */}
      <section style={{padding:'96px 24px',borderTop:'1px solid #1f2937'}}>
        <div style={{maxWidth:'900px',margin:'0 auto'}}>
          <h2 style={{fontSize:'32px',fontWeight:'700',textAlign:'center',marginBottom:'64px'}}>How it works</h2>
          <div style={{display:'grid',gridTemplateColumns:'repeat(auto-fit,minmax(200px,1fr))',gap:'32px'}}>
            {[
              {step:'01',title:'Connect wallet',desc:'Sign in with Phantom. Your wallet is your identity.'},
              {step:'02',title:'Add your team',desc:'Add contributors by wallet address. Set payment amounts and schedules.'},
              {step:'03',title:'Funds earn yield',desc:'Idle payroll funds earn yield automatically via Reflect.'},
              {step:'04',title:'Pay and advance',desc:'Contributors get paid on schedule — or advance instantly. Zero fees.'},
            ].map((item) => (
              <div key={item.step} style={{textAlign:'center'}}>
                <div style={{fontSize:'40px',fontWeight:'700',color:'#374151',marginBottom:'16px'}}>{item.step}</div>
                <h3 style={{fontWeight:'600',fontSize:'18px',marginBottom:'8px'}}>{item.title}</h3>
                <p style={{color:'#9ca3af',fontSize:'14px',lineHeight:'1.6'}}>{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Built on Solana */}
      <section style={{padding:'96px 24px',borderTop:'1px solid #1f2937',textAlign:'center'}}>
        <div style={{maxWidth:'600px',margin:'0 auto'}}>
          <h2 style={{fontSize:'32px',fontWeight:'700',marginBottom:'24px'}}>Built on Solana</h2>
          <p style={{color:'#9ca3af',marginBottom:'48px',lineHeight:'1.7'}}>
            Sub-second settlement. Near-zero fees. Composable with Phantom, Squads, and Reflect natively. No other chain makes this viable at this cost and speed.
          </p>
          <div style={{display:'flex',flexWrap:'wrap',justifyContent:'center',gap:'12px'}}>
            {['Phantom','Squads','Reflect','Helius','Anchor'].map((tech) => (
              <span key={tech} style={{border:'1px solid #1f2937',padding:'8px 20px',borderRadius:'999px',fontSize:'14px',color:'#6b7280'}}>
                {tech}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer style={{padding:'48px 24px',borderTop:'1px solid #1f2937',textAlign:'center',color:'#4b5563',fontSize:'14px'}}>
        <p>Paycheck by White Claw — Built for Colosseum Frontier 2026</p>
        <p style={{marginTop:'8px'}}>
          <a href="https://twitter.com/whiteclawonsol" style={{color:'#6b7280',textDecoration:'none'}}>@whiteclawonsol</a>
          {' · '}$WCLAW
        </p>
      </footer>
    </main>
  );
}
