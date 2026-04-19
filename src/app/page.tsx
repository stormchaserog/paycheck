export default function Home() {
  return (
    <main className="min-h-screen bg-black text-white">
      {/* Hero */}
      <section className="flex flex-col items-center justify-center min-h-screen px-6 text-center">
        <div className="max-w-3xl mx-auto">
          <p className="text-sm uppercase tracking-widest text-gray-400 mb-6">
            White Claw — Crypto-Native Fintech
          </p>
          <h1 className="text-5xl md:text-7xl font-bold tracking-tight mb-6">
            Paycheck
          </h1>
          <p className="text-xl md:text-2xl text-gray-300 mb-4">
            Stablecoin payroll with yield-powered advances
            for crypto-native teams.
          </p>
          <p className="text-gray-500 mb-12 max-w-xl mx-auto">
            Set up your team once. Funds earn yield automatically.
            Contributors get paid on schedule — and can advance their
            next paycheck instantly at zero cost.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="bg-white text-black font-semibold px-8 py-4 rounded-lg hover:bg-gray-100 transition">
              Get Early Access
            </button>
            <button className="border border-gray-700 text-white font-semibold px-8 py-4 rounded-lg hover:border-gray-500 transition">
              Watch Demo
            </button>
          </div>
        </div>
      </section>

      {/* How it works */}
      <section className="px-6 py-24 border-t border-gray-800">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-3xl font-bold text-center mb-16">How it works</h2>
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            {[
              { step: "01", title: "Connect wallet", desc: "Sign in with Phantom. Your wallet is your identity." },
              { step: "02", title: "Add your team", desc: "Add contributors by wallet address. Set payment amounts and schedules." },
              { step: "03", title: "Funds earn yield", desc: "Idle payroll funds earn yield automatically via Reflect." },
              { step: "04", title: "Pay and advance", desc: "Contributors get paid on schedule — or advance instantly. Zero fees." },
            ].map((item) => (
              <div key={item.step} className="text-center">
                <div className="text-4xl font-bold text-gray-700 mb-4">{item.step}</div>
                <h3 className="font-semibold text-lg mb-2">{item.title}</h3>
                <p className="text-gray-400 text-sm">{item.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Built on Solana */}
      <section className="px-6 py-24 border-t border-gray-800 text-center">
        <div className="max-w-2xl mx-auto">
          <h2 className="text-3xl font-bold mb-6">Built on Solana</h2>
          <p className="text-gray-400 mb-12">
            Sub-second settlement. Near-zero fees. Composable with Phantom,
            Squads, and Reflect natively. No other chain makes this viable
            at this cost and speed.
          </p>
          <div className="flex flex-wrap justify-center gap-4 text-sm text-gray-500">
            {["Phantom", "Squads", "Reflect", "Helius", "Anchor"].map((tech) => (
              <span key={tech} className="border border-gray-800 px-4 py-2 rounded-full">
                {tech}
              </span>
            ))}
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="px-6 py-12 border-t border-gray-800 text-center text-gray-600 text-sm">
        <p>Paycheck by White Claw — Built for Colosseum Frontier 2026</p>
        <p className="mt-2">
          <a href="https://twitter.com/whiteclawonsol" className="hover:text-gray-400 transition">
            @whiteclawonsol
          </a>
          {" · "}$WCLAW
        </p>
      </footer>
    </main>
  );
}
