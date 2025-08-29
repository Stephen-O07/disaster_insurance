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

![Architecture Diagram](https://github.com/Stephen-O07/disaster_insurance/blob/c05f86a18425ba5c6d43d5a645eaf0f6de263238/asset/ArchitectureDiagram.gif)

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




