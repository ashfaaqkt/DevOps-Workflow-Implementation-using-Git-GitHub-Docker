
# DevOps Workflow Implementation using Git, GitHub & Docker

This project demonstrates a complete **DevOps workflow**, including version control with Git, remote repository integration using GitHub, and application containerization using Docker. It covers creating a static website, managing it with Git, pushing the project to GitHub, building a Docker image for a Flask application, and running the app inside a Docker container.

---

## 📌 Project Details  
**Author:** Ashfaaq Feroz Muhammad  
**ID:** 2023EBCS005  
**Year:** 2025  
**Course:** SGA2 – Software Development Practices  

---

## 🚀 Technologies & Languages Used

### **Languages**
- HTML  
- CSS  
- Python (Flask)

### **Technologies & Tools**
- Git  
- GitHub  
- Docker & Docker Hub  
- VS Code  
- Linux/CLI Terminal  
- Docker Desktop  

---

## 🧩 Part 1 — Git & GitHub

A simple static website was created using **HTML and CSS**:
- `index.html`
- `about.html`
- `contact.html`
- `style.css`

A local Git repository was initialized:

```bash
git init

Key Git commands demonstrated:
	•	git status
	•	git add .
	•	git commit -m "Initial commit"
	•	git log --oneline -n 3
	•	git branch feature/update-readme
	•	git switch feature/update-readme
	•	git switch main

GitHub Integration

A new GitHub repository was created and connected via:

git remote add origin <repo-url>
git push -u origin main

GitHub Repository Link:
https://github.com/ashfaaqkt/devops-assignment-starter

Screenshots in the report show successful pushes and remote sync (Page 6)  ￼.

⸻

🐳 Part 2 — Docker Containerization

A Python Flask application was developed to display:

Hello, World! 👋 (served from a Docker container)

Dockerfile Used

FROM python:3.12-slim
WORKDIR /app
RUN python -m pip install --upgrade pip && python -m pip install flask==3.0.3 --no-cache-dir
COPY app.py /app/app.py
EXPOSE 8080
CMD ["python", "app.py"]

Docker Workflow

1. Build Docker Image

docker build --no-cache -t ashfaaqkt/hello-app:1.0 .

2. Push Image to Docker Hub

docker login
docker tag ashfaaqkt/hello-app:1.0 ashfaaqkt/hello-app:latest
docker push ashfaaqkt/hello-app:1.0
docker push ashfaaqkt/hello-app:latest

Docker Hub Repository:
https://hub.docker.com/repository/docker/ashfaaqkt/hello-app

3. Run the Docker Container Locally

docker run -d -p 8080:8080 --name hello1 ashfaaqkt/hello-app:1.0
docker ps

Application was accessible at:
http://localhost:8080
(See final page screenshot where the Flask app runs in the browser)  ￼.

⸻

✅ Summary

This project successfully demonstrates:
	•	Git version control
	•	GitHub repository management
	•	Docker image creation
	•	Containerization of a Python Flask application
	•	Running containers locally
	•	Publishing images on Docker Hub
	•	Practical DevOps workflow aligned with real-world CI/CD practices

The included screenshots throughout the report validate the execution of every step.

⸻

📄 Screenshots

All screenshots referenced in the report are available in the PDF and in the “screenshots” folder.

⸻

👤 Author

Ashfaaq Feroz Muhammad
SGA2 – Software Development Practices
2025
