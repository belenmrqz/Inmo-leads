import Link from "next/link";
import { notFound } from "next/navigation";

import { getPromocion } from "../../../lib/api";

export const maxDuration = 60;

const euros = new Intl.NumberFormat("es-ES", {
  style: "currency",
  currency: "EUR",
  maximumFractionDigits: 0,
});

export default async function PromocionPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;
  const promocion = await getPromocion(id);

  if (!promocion) {
    notFound();
  }

  return (
    <main className="mx-auto max-w-3xl px-6 py-12">
      <Link href="/" className="text-sm text-gray-500 hover:underline">
        ← Volver a las promociones
      </Link>

      <header className="mt-6">
        <div className="flex flex-wrap items-center gap-3">
          <h1 className="text-3xl font-bold tracking-tight">{promocion.nombre}</h1>
          {promocion.es_vpo && (
            <span className="rounded-full bg-emerald-100 px-3 py-1 text-xs font-medium text-emerald-800">
              VPO
            </span>
          )}
        </div>
        <p className="mt-1 text-gray-500">{promocion.zona}</p>
      </header>

      <p className="mt-6 text-lg text-gray-700 dark:text-gray-300">
        {promocion.descripcion}
      </p>

      <dl className="mt-10 grid gap-4 sm:grid-cols-3">
        <div className="rounded-xl border border-gray-200 p-5 dark:border-gray-800">
          <dt className="text-xs uppercase text-gray-500">Precio desde</dt>
          <dd className="mt-1 text-2xl font-bold">
            {euros.format(Number(promocion.precio_desde))}
          </dd>
        </div>
        <div className="rounded-xl border border-gray-200 p-5 dark:border-gray-800">
          <dt className="text-xs uppercase text-gray-500">Tipo</dt>
          <dd className="mt-1 text-2xl font-bold">
            {promocion.es_vpo ? "Protección oficial" : "Vivienda libre"}
          </dd>
        </div>
        <div className="rounded-xl border border-gray-200 p-5 dark:border-gray-800">
          <dt className="text-xs uppercase text-gray-500">Viviendas</dt>
          <dd className="mt-1 text-2xl font-bold">
            {promocion.num_viviendas ?? "Por confirmar"}
          </dd>
        </div>
      </dl>
    </main>
  );
}