# Gestionnaire de tâches étudiant

Un gestionnaire de tâches simple pour les étudiants. Ajoute tes devoirs avec
une matière et une date limite, coche-les quand ils sont terminés, et vois
d’un coup d’œil ce qui est en retard. Réalisé avec les bases de Python (Flask),
HTML et CSS.

## Fonctionnalités
- Ajouter une tâche avec un titre, une matière et une date limite
- Marquer une tâche comme terminée (ou annuler), et la supprimer
- Les tâches en retard sont surlignées en rouge
- Les tâches sont enregistrées dans `tasks.json`, elles sont donc retrouvées à la prochaine ouverture

## Comment le lancer
1. Installe Python 3 depuis https://www.python.org
2. Télécharge ou clone ce projet :
   ```
   git clone https://github.com/TON-PSEUDO/uni-task-manager.git
   cd uni-task-manager
   ```
3. Installe Flask :
   ```
   pip install -r requirements.txt
   ```
4. Démarre l’application :
   ```
   python app.py
   ```
5. Ouvre http://127.0.0.1:5000 dans ton navigateur.

## Structure du projet
```
uni-task-manager/
├── app.py              # Python : la logique (ajouter, terminer, supprimer)
├── templates/
│   └── index.html      # HTML : la page
├── static/
│   └── style.css       # CSS : l’apparence
├── requirements.txt    # Paquets Python nécessaires
└── README.md
```

## Idées pour aller plus loin
- Ajouter un niveau de priorité (faible / moyenne / haute)
- Ajouter un filtre pour n’afficher qu’une seule matière
- Ajouter une page pour modifier une tâche
