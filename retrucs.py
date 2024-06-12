import random

# Llista de retrucs en català
retrucs_cat = [
    {
        "text": '''A quien madruga,
Dios le ayuda.''',
        "autor": "Desconegut",
        "idioma": "CAT"
    },
    {
        "text": '''Qui no vulgui pols,
que no vagi a l’era.''',
        "autor": "Desconegut",
        "idioma": "CAT"
    }
]

# Llista de retrucs en castellà
retrucs_esp = [
    {
        "text": '''A quien madruga,
Dios le ayuda.''',
        "autor": "Desconocido",
        "idioma": "ESP"
    },
    {
        "text": '''Más vale tarde
que nunca.''',
        "autor": "Desconocido",
        "idioma": "ESP"
    }
]

# Llista de retrucs en anglès
retrucs_eng = [
    {
        "text": '''The early bird
catches the worm.''',
        "autor": "Unknown",
        "idioma": "ENG"
    },
    {
        "text": '''Better late
than never.''',
        "autor": "Unknown",
        "idioma": "ENG"
    }
]

# Unir todas las listas de retrucs
retrucs = retrucs_cat + retrucs_esp + retrucs_eng

# Preguntar idioma a l'usuari
idioma_desitjat = input("En quin idioma vols veure els retrucs? (CAT/ENG/ESP): ").strip().upper()

# Filtrar els retrucs per l'idioma seleccionat
retrucs_filtrats = [retruc for retruc in retrucs if retruc["idioma"] == idioma_desitjat]

# Verificar si hi ha retrucs en l'idioma seleccionat
if not retrucs_filtrats:
    print(f"No hi ha retrucs disponibles en l'idioma '{idioma_desitjat}'.")
else:
    # Seleccionar els retrucs a l'atzar (encara que només n'hi ha dos per idioma en aquest cas)
    retrucs_seleccionats = random.sample(retrucs_filtrats, min(10, len(retrucs_filtrats)))

    # Ordenar els retrucs seleccionats alfabèticament pel text
    retrucs_ordenats = sorted(retrucs_seleccionats, key=lambda x: x["text"])

    # Mostrar els retrucs ordenats
    for retruc in retrucs_ordenats:
        print(f'{retruc["text"]} - {retruc["autor"]} (Idioma: {retruc["idioma"]})\n')

