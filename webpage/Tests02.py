
import os
import sqlite3
import pandas as pd

# Tabellen:
# logs_raw, shipments

# Spalten:  shipment_id, timestamp, severity, thread, source, event, station, box_barcode, articles, exp_weight_kg
#           act_weight_kg, tare_weight_kg, product_weight_kg, abs_weight_diff, print_quality_pct, line_speed_mps
#           slam, iso_grade, pckg_problem_found, weight_diff, weight_diff_ratio, distance_to_threshold, is_kot

### Datenbankverbindung herstellen
def db_connection():
    db_path = r"C:\Users\micha\Documents\Projets_Abschlussarbeit\Proj_Machine-Log-Navigator\MLN-normalized\label_machine.db"
    if not os.path.exists(db_path):
        print("Datenbank 'label_machine' fehlt!\n'Bitte prüfe Pfad und ob die Datei existiert!")
        exit()

    connection = sqlite3.connect(db_path)
    return connection

db_con = db_connection()
with db_con:
    df = pd.read_sql_query(
        "SELECT * FROM shipments ORDER BY timestamp;",
        db_con
    )
df.to_csv('datenbank_export.csv', index=False, sep='|', encoding='utf-8-sig')


