Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
    - `example_astronauts`: This DAG shows a simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. The DAG uses the TaskFlow API to define tasks in Python, and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see our [Getting started tutorial](https://www.astronomer.io/docs/learn/get-started-with-airflow).
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

Start Airflow on your local machine by running 'astro dev start'.

This command will spin up five Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- DAG Processor: The Airflow component responsible for parsing DAGs
- API Server: The Airflow component responsible for serving the Airflow UI and API
- Triggerer: The Airflow component responsible for triggering deferred tasks

When all five containers are ready the command will open the browser to the Airflow UI at http://localhost:8080/. You should also be able to access your Postgres Database at 'localhost:5432/postgres' with username 'postgres' and password 'postgres'.

<<<<<<< HEAD
Note: If you already have either of the above ports allocated, you can either [stop your existing Docker containers or change the port](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).
=======
* **Company Context:** ResilienceWatch Analytics in partnership with SafeGuard Insurance.
* **Problem:** Fragmented claims and disaster event data, lack of real-time insights, slow claims resolution.
* **Solution:** A Dockerized Python ETL pipeline that integrates FEMA API disaster data with a Postgres database, automated with CI/CD, and visualized in Power BI.

---

## 4. **Architecture**

**Flow:**
FEMA API  → PostgreSQL (Dockerized) → Power BI

**Components:**

* `extract.py`: Fetches FEMA data via API.
* `db_connect.py`: Creates DB connection (PostgreSQL) & disaster table.
* `main.py`: Orchestrates extract → load process.
* Postgres + pgAdmin (Dockerized).
* GitHub Actions workflow for Docker build/push.

![image alt](https://github.com/Stephen-O07/disaster_insurance/blob/55ef0f7c46dfd369efe1ae530a244fedb6e25e63/ArchitectureDiagram.gif)

---

## 5. **Features / Business Logic**

* Automated ingestion of FEMA Public Assistance Funded Projects data.
* Deduplication with composite primary key (`disasterNumber`, `pwNumber`).
* KPI tracking for:

  1. Funding by Disaster Type
  2. Project Status Performance
  3. Resolution Time Analysis
  4. Funding by Damage Category
  5. Geographic Disaster Impact

---

## 6. **Tech Stack**

* **Python**: ETL (requests, psycopg2, dotenv).
* **PostgreSQL**: Relational database for disaster data.
* **Docker & Docker Compose**: Containerization.
* **Power BI**: Visualization and dashboards.
* **GitHub Actions**: CI/CD pipeline for Docker builds.

---

## 7. **Setup Instructions**

### Prerequisites

* Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
* Install Python 3.11+
* Install Power BI Desktop (for dashboarding)

### Clone Repo

```bash
git clone https://github.com/<your-username>/disaster_insurance.git
cd disaster_insurance
```

### Environment Variables

Create a `.env` file:

```ini
API_URL=https://www.fema.gov/api/open/v2/PublicAssistanceFundedProjectsDetails
HOST=postgres
PORT=5432
DATABASE=disaster_insurance
USER=admin
PASSWORD=admin
```

### Build & Run with Docker Compose

```bash
docker compose up -d
```

---

## 8. **Running the Pipeline**

1. Start Postgres & pgAdmin via Docker Compose.
2. Run ETL:

   ```bash
   python main.py
   ```

   (or package Python into Docker and run inside container).
3. Verify table in Postgres:

   ```sql
   SELECT * FROM disaster LIMIT 10;
   ```

---

## 9. **Power BI Dashboard**

Connect Power BI to PostgreSQL and create visuals:

* **Bar Chart**: Funding by Disaster Type
* **Donut Chart**: Project Status distribution
* **Line Chart**: Avg Resolution Time by Disaster
* **Stacked Bar**: Funding by Damage Category + Project Size
* **Map**: Obligated funds by State/County

---

## 🔟 **CI/CD with GitHub Actions**

* Workflow file: `.github/workflows/docker-deploy.yml`
* Automates:

  * Docker image build (`python:3.12-slim` base).
  * Push to DockerHub using `DOCKERHUB_USERNAME` + `DOCKERHUB_TOKEN` secrets.

---

## 11. **Project Structure**

```plaintext
disaster_insurance/
│── elt/
│   ├── db_connect.py      # PostgreSQL connection & schema
│   ├── extract.py         # API extraction logic
│── main.py                # ETL orchestration
│── requirements.txt       # Python dependencies
│── Dockerfile             # Python app container
│── compose.yml            # Postgres + pgAdmin services
│── .env                   # Environment variables
│── .dockerignore          # Ignore unnecessary files in Docker build
│── .github/workflows/     
│   └── docker-deploy.yml  # CI/CD pipeline
```

---
>>>>>>> fe7b29356d5adc901a47d3cf7c11f00b53428b40

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://www.astronomer.io/docs/astro/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.
















# *Disaster Insurance Analytics*



## 1. **Project Title & Description**

**Disaster Insurance Analytics – Disaster Response KPI Dashboard**
An end-to-end ETL pipeline and analytics solution that ingests FEMA disaster data, loads it into PostgreSQL, and enables interactive dashboards (Power BI) for insurance claim insights.

---

## 2. **Table of Contents**

* Overview
* Architecture
* Features / Business Logic
* Tech Stack
* Setup Instructions
* Running the Pipeline
* Power BI Dashboard
* CI/CD with GitHub Actions
* Project Structure
* License

---

## 3. **Overview**

* **Company Context:** ResilienceWatch Analytics in partnership with SafeGuard Insurance.
* **Problem:** Fragmented claims and disaster event data, lack of real-time insights, slow claims resolution.
* **Solution:** A Dockerized Python ETL pipeline that integrates FEMA API disaster data with a Postgres database, automated with CI/CD, and visualized in Power BI.

---

## 4. **Architecture**

**Flow:**
FEMA API  → PostgreSQL (Dockerized) → Power BI

**Components:**

* `extract.py`: Fetches FEMA data via API.
* `db_connect.py`: Creates DB connection (PostgreSQL) & disaster table.
* `main.py`: Orchestrates extract → load process.
* Postgres + pgAdmin (Dockerized).
* GitHub Actions workflow for Docker build/push.

![Architecture Diagram](ArchutectureDiagram.gif)

---

## 5. **Features / Business Logic**

* Automated ingestion of FEMA Public Assistance Funded Projects data.
* Deduplication with composite primary key (`disasterNumber`, `pwNumber`).
* KPI tracking for:

  1. Funding by Disaster Type
  2. Project Status Performance
  3. Resolution Time Analysis
  4. Funding by Damage Category
  5. Geographic Disaster Impact

---

## 6. **Tech Stack**

* **Python**: ETL (requests, psycopg2, dotenv).
* **PostgreSQL**: Relational database for disaster data.
* **Docker & Docker Compose**: Containerization.
* **Power BI**: Visualization and dashboards.
* **GitHub Actions**: CI/CD pipeline for Docker builds.

---

## 7. **Setup Instructions**

### Prerequisites

* Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
* Install Python 3.11+
* Install Power BI Desktop (for dashboarding)

### Clone Repo

```bash
git clone https://github.com/<your-username>/disaster_insurance.git
cd disaster_insurance
```

### Environment Variables

Create a `.env` file:

```ini
API_URL=https://www.fema.gov/api/open/v2/PublicAssistanceFundedProjectsDetails
HOST=postgres
PORT=5432
DATABASE=disaster_insurance
USER=admin
PASSWORD=admin
```

### Build & Run with Docker Compose

```bash
docker compose up -d
```

---

## 8. **Running the Pipeline**

1. Start Postgres & pgAdmin via Docker Compose.
2. Run ETL:

   ```bash
   python main.py
   ```

   (or package Python into Docker and run inside container).
3. Verify table in Postgres:

   ```sql
   SELECT * FROM disaster LIMIT 10;
   ```

---

## 9. **Power BI Dashboard**

Connect Power BI to PostgreSQL and create visuals:

* **Bar Chart**: Funding by Disaster Type
* **Donut Chart**: Project Status distribution
* **Line Chart**: Avg Resolution Time by Disaster
* **Stacked Bar**: Funding by Damage Category + Project Size
* **Map**: Obligated funds by State/County

---

## 🔟 **CI/CD with GitHub Actions**

* Workflow file: `.github/workflows/docker-deploy.yml`
* Automates:

  * Docker image build (`python:3.12-slim` base).
  * Push to DockerHub using `DOCKERHUB_USERNAME` + `DOCKERHUB_TOKEN` secrets.

---

## 11. **Project Structure**

```plaintext
disaster_insurance/
│── elt/
│   ├── db_connect.py      # PostgreSQL connection & schema
│   ├── extract.py         # API extraction logic
│── main.py                # ETL orchestration
│── requirements.txt       # Python dependencies
│── Dockerfile             # Python app container
│── compose.yml            # Postgres + pgAdmin services
│── .env                   # Environment variables
│── .dockerignore          # Ignore unnecessary files in Docker build
│── .github/workflows/     
│   └── docker-deploy.yml  # CI/CD pipeline
```

---




