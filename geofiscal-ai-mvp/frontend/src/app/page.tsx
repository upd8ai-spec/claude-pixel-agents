export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100 p-8">
      <h1 className="text-4xl font-semibold">GeoFiscal AI Command Center</h1>
      <p className="mt-3 text-slate-300">Executive-grade geographic financial intelligence and reconciliation.</p>
      <section className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-8">
        {['Total Budget','Utilized','Risk Index'].map((k) => (
          <div key={k} className="rounded-xl border border-slate-800 bg-slate-900/70 p-4">
            <h3 className="text-sm text-slate-400">{k}</h3>
            <p className="text-2xl font-bold mt-2">—</p>
          </div>
        ))}
      </section>
    </main>
  );
}
