# Gestionnaire de tâches pour étudiants - une petite application de to-do list.
# Lancer avec :  python app.py   puis ouvrir http://127.0.0.1:5000

import json
import os
from datetime import date

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
DATA_FILE = "tasks.json"  # les tâches sont enregistrées ici, elles survivent au redémarrage


def load_tasks():
    """Lit la liste des tâches dans le fichier JSON (liste vide s'il n'existe pas encore)."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    """Écrit la liste des tâches dans le fichier JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


@app.template_filter("date_fr")
def date_fr(iso_date):
    """Transforme 2026-11-08 en 08/11/2026 pour l'affichage."""
    annee, mois, jour = iso_date.split("-")
    return f"{jour}/{mois}/{annee}"


@app.route("/")
def index():
    tasks = load_tasks()
    # Les tâches non terminées d'abord, puis la date limite la plus proche en premier
    tasks.sort(key=lambda t: (t["done"], t["due"] or "9999-12-31"))
    return render_template("index.html", tasks=tasks, today=date.today().isoformat())


@app.route("/add", methods=["POST"])
def add():
    title = request.form["title"].strip()
    if title:
        tasks = load_tasks()
        new_id = max([t["id"] for t in tasks], default=0) + 1
        tasks.append({
            "id": new_id,
            "title": title,
            "course": request.form["course"].strip(),
            "due": request.form["due"],  # "" si l'étudiant n'a pas mis de date
            "done": False,
        })
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    tasks = [t for t in load_tasks() if t["id"] != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
