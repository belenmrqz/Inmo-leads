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

export async function getPromocion(id: string): Promise<Promocion | null> {
  const res = await fetch(`${API_URL}/promociones/${id}`, { cache: "no-store" });
  // 404: no existe. 422: el id no es un número (por ejemplo /promociones/abc)
  if (res.status === 404 || res.status === 422) {
    return null;
  }
  if (!res.ok) {
    throw new Error("No se pudo cargar la promoción");
  }
  return res.json();
}