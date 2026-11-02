import { getPromociones } from "../lib/api";

const euros = new Intl.NumberFormat("es-ES", {
  style: "currency",
  currency: "EUR",
  maximumFractionDigits: 0,
});

export default async function Home() {
  const promociones = await getPromociones();

  return (
    <main className="mx-auto max-w-6xl px-6 py-12">
      <header className="mb-10">
        <h1 className="text-3xl font-bold tracking-tight">Nuestras promociones</h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          Viviendas de obra nueva y de protección oficial en el entorno de Sevilla.
        </p>
      </header>

      <section className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {promociones.map((p) => (
          <article
            key={p.id}
            className="flex flex-col rounded-xl border border-gray-200 p-6 shadow-sm dark:border-gray-800"
          >
            <div className="flex items-start justify-between gap-3">
              <h2 className="text-lg font-semibold">{p.nombre}</h2>
              {p.es_vpo && (
                <span className="rounded-full bg-emerald-100 px-3 py-1 text-xs font-medium text-emerald-800">
                  VPO
                </span>
              )}
            </div>

            <p className="mt-1 text-sm text-gray-500">{p.zona}</p>
            <p className="mt-4 flex-1 text-sm text-gray-600 dark:text-gray-400">
              {p.descripcion}
            </p>

            <div className="mt-6 flex items-end justify-between">
              <div>
                <p className="text-xs uppercase text-gray-500">Desde</p>
                <p className="text-xl font-bold">
                  {euros.format(Number(p.precio_desde))}
                </p>
              </div>
              {p.num_viviendas !== null && (
                <p className="text-sm text-gray-500">{p.num_viviendas} viviendas</p>
              )}
            </div>
          </article>
        ))}
      </section>
    </main>
  );
}