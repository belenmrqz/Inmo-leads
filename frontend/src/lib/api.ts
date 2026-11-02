const API_URL = process.env.API_URL ?? "http://127.0.0.1:8000";

export type Promocion = {
  id: number;
  nombre: string;
  descripcion: string | null;
  zona: string;
  es_vpo: boolean;
  precio_desde: string;
  num_viviendas: number | null;
};

export async function getPromociones(): Promise<Promocion[]> {
  const res = await fetch(`${API_URL}/promociones`, { cache: "no-store" });
  if (!res.ok) {
    throw new Error("No se pudieron cargar las promociones");
  }
  return res.json();
}