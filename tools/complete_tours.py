#!/usr/bin/env python3
"""Riempie il campo `options` di zz_users con l'array completo degli id dei moduli
presenti in zz_modules, nel formato {"tours":[1,2,3,...]}, per completare il Tour
del gestionale openSTAManager.

Uso:
    python tools/complete_tours.py            # aggiorna tutti gli utenti
    python tools/complete_tours.py admin      # aggiorna solo l'utente 'admin'
"""

import json
import os
import sys

import pymysql

CONFIG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "config.json")


def load_db_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    db = config["database"]
    return {
        "host": db.get("host", "localhost"),
        "user": db.get("user", "root"),
        "password": db.get("pass", ""),
        "database": db.get("name", "openstamanager"),
        "charset": "utf8mb4",
        "cursorclass": pymysql.cursors.DictCursor,
    }


def main():
    username = sys.argv[1] if len(sys.argv) > 1 else None

    conn = pymysql.connect(**load_db_config())
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT `id` FROM `zz_modules` ORDER BY `id`")
            module_ids = [row["id"] for row in cursor.fetchall()]

            if not module_ids:
                print("Nessun modulo trovato in zz_modules: operazione annullata.")
                sys.exit(1)

            tours = json.dumps({"tours": module_ids}, separators=(",", ":"))
            print(f"Trovati {len(module_ids)} moduli: {tours}")

            if username:
                cursor.execute(
                    "SELECT `id`, `options` FROM `zz_users` WHERE `username` = %s",
                    (username,),
                )
            else:
                cursor.execute("SELECT `id`, `options` FROM `zz_users`")

            users = cursor.fetchall()
            if not users:
                print(f"Nessun utente trovato{' per ' + username if username else ''}.")
                sys.exit(1)

            for user in users:
                try:
                    options = json.loads(user["options"]) if user["options"] else {}
                    if not isinstance(options, dict):
                        options = {}
                except (TypeError, ValueError):
                    options = {}

                options["tours"] = module_ids
                cursor.execute(
                    "UPDATE `zz_users` SET `options` = %s WHERE `id` = %s",
                    (json.dumps(options, separators=(",", ":")), user["id"]),
                )
                print(f"Utente '{user['id']}' aggiornato.")

        conn.commit()
        print(f"Completato: campo options aggiornato per {len(users)} utenti.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
