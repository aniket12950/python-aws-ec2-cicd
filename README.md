# Python AWS EC2 CI/CD Deployment

A simple Python project demonstrating **Continuous Integration and Continuous Deployment (CI/CD)** using **GitHub Actions** and **AWS EC2**.

Whenever code is pushed to the `main` branch, GitHub Actions automatically:

1. Checks out the latest source code.
2. Sets up Python 3.11.
3. Installs project dependencies.
4. Runs the Python application.
5. Connects to an AWS EC2 instance using SSH.
6. Pulls the latest code from GitHub.
7. Executes the deployment script on EC2.

## 🚀 Project Architecture

```text
Developer
    │
    │ git push
    ▼
GitHub Repository
    │
    ▼
GitHub Actions
    │
    ├── Checkout Code
    ├── Setup Python 3.11
    ├── Install Dependencies
    ├── Run Python Application
    │
    ▼
SSH Connection
    │
    ▼
AWS EC2
    │
    ├── git pull
    └── deploy.py
```

## 🛠️ Technologies Used

* **Python 3.11**
* **AWS EC2**
* **GitHub**
* **GitHub Actions**
* **Git**
* **Linux**
* **SSH**
* **CI/CD**

## 📁 Project Structure

```text
python-aws-ec2-cicd/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app.py
├── deploy.py
├── students.json
├── requirements.txt
├── .gitignore
└── README.md
```

## 📌 Application

The Python application reads student information from `students.json` and identifies the student with the highest marks.

Example:

```text
===== Student Report =====
Topper : Rahul
Marks  : 95
```

## ⚙️ How the CI/CD Pipeline Works

The GitHub Actions workflow is triggered whenever code is pushed to the `main` branch.

### Step 1: Checkout Code

GitHub Actions downloads the latest repository code.

### Step 2: Setup Python

Python 3.11 is configured using the `actions/setup-python` action.

### Step 3: Install Dependencies

The workflow executes:

```bash
pip install -r requirements.txt
```

### Step 4: Run Application

The application is tested using:

```bash
python app.py
```

### Step 5: Connect to AWS EC2

GitHub Actions connects to the EC2 instance using SSH.

The following GitHub Secrets are used:

```text
EC2_HOST
EC2_USERNAME
PRIVATE_KEY
```

### Step 6: Deploy Latest Code

After connecting to EC2, the workflow executes:

```bash
cd ~/python-aws-ec2-cicd
git pull origin main
python3 deploy.py
```

## 🔐 GitHub Secrets

Before running the pipeline, configure the following secrets in:

**GitHub Repository → Settings → Secrets and variables → Actions**

| Secret         | Description                          |
| -------------- | ------------------------------------ |
| `EC2_HOST`     | Public IP address or hostname of EC2 |
| `EC2_USERNAME` | EC2 SSH username                     |
| `PRIVATE_KEY`  | EC2 private SSH key                  |

> Never commit your `.pem` private key or other credentials to GitHub.

## ☁️ AWS EC2 Setup

Launch an EC2 instance with a Linux-based operating system.

Install Git and Python:

```bash
sudo apt update
sudo apt install git python3 -y
```

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-aws-ec2-cicd.git
```

Move into the project:

```bash
cd python-aws-ec2-cicd
```

Run the application:

```bash
python3 app.py
```

Run the deployment script:

```bash
python3 deploy.py
```

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-aws-ec2-cicd.git
```

Navigate to the project:

```bash
cd python-aws-ec2-cicd
```

Run:

```bash
python app.py
```

## 🔄 Trigger CI/CD

After making changes:

```bash
git add .
git commit -m "Update Python application"
git push origin main
```

GitHub Actions will automatically start the deployment workflow.

You can monitor the workflow from:

```text
GitHub Repository
→ Actions
→ Python CI/CD
```

## 🎯 Learning Objectives

This project demonstrates:

* Python application execution
* Git and GitHub version control
* GitHub Actions workflows
* CI/CD automation
* AWS EC2 deployment
* SSH-based remote deployment
* GitHub Actions Secrets
* Basic DevOps workflow


---

⭐ If you find this project useful, consider giving the repository a star.
