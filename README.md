# Midterm Project 

A two-app system that collects user feedback and tracks page visits.
Both apps share a single Redis database.

- App 1 (Message Collector): submits messages and counts page visits
- App 2 (Dashboard): displays the total messages and total visits
- Redis: stores the data (with persistence enabled)

## How to run

Make sure Docker Desktop is running, then from the project folder:

```
docker compose up --build
```

Then open:

- App 1: http://localhost:5001
- App 2: http://localhost:5002

To stop:

```
docker compose down
```

## Project structure

```
midterm-project/
├── app1-collector/             - message collector app
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/index.html
├── app2-dashboard/             - dashboard app
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/index.html
├── docker-compose.yml          - runs all 3 services
└── README.md
```

See the project report (Project_Report.docx) for the full explanation.