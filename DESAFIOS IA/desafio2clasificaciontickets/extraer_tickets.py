"""Extrae tickets de un texto sin procesar y los guarda en Excel.
Uso: python extraer_tickets.py tickets_crudos.txt tickets.xlsx
Requiere: pip install openpyxl
"""
import re
import sys
from openpyxl import Workbook

PATRON = re.compile(
    r"\[(?P<fecha>[\d\- :]+)\]\s*TICKET #(?P<id>\d+)\s*\|\s*usuario:\s*(?P<usuario>\S+)\s*\|\s*mensaje:\s*(?P<mensaje>.+)"
)

def extraer(texto):
    return [m.groupdict() for m in PATRON.finditer(texto)]

def guardar_excel(tickets, ruta):
    wb = Workbook()
    ws = wb.active
    ws.title = "Tickets"
    ws.append(["ID", "Fecha", "Usuario", "Mensaje", "Tipo de incidencia"])
    for t in tickets:
        ws.append([int(t["id"]), t["fecha"], t["usuario"], t["mensaje"].strip(), ""])
    for col, ancho in zip("ABCDE", (8, 18, 14, 80, 22)):
        ws.column_dimensions[col].width = ancho
    wb.save(ruta)

if __name__ == "__main__":
    entrada = sys.argv[1] if len(sys.argv) > 1 else "tickets_crudos.txt"
    salida = sys.argv[2] if len(sys.argv) > 2 else "tickets.xlsx"
    with open(entrada, encoding="utf-8") as f:
        tickets = extraer(f.read())
    guardar_excel(tickets, salida)
    print(f"{len(tickets)} tickets guardados en {salida}")
