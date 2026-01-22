# HeJoTarget 🎯

**Advanced Full-Stack Penetration Testing Training Platform**

HeJoTarget is a comprehensive, automated vulnerability laboratory designed for security researchers and penetration testing students. It deploys a multi-layered infrastructure via Docker, simulating real-world misconfigurations and web vulnerabilities.

## 🚀 Features

HeJoTarget provides an integrated environment consisting of several attack surfaces:

* **Web Layer:** A modern PHP-based interface featuring "Glassmorphism" design.
* **Infrastructure:** Live services including SSH, FTP, SMB, and Redis.
* **Automation:** A Python-based deployment script that handles Docker image building, container networking, and cleanup.
* **Interactive Console:** A built-in "Command Center" to execute commands directly inside the target environment.



<img width="1089" height="519" alt="resim" src="https://github.com/user-attachments/assets/4b9be0b7-1623-467d-a87b-bfd714e93c91" />




<img width="1034" height="501" alt="resim" src="https://github.com/user-attachments/assets/8120fd4f-f2e2-48ea-be2d-691da23cda4f" />




<img width="1509" height="819" alt="resim" src="https://github.com/user-attachments/assets/cb7d4769-03dd-4ff4-85c0-99f7694a7f61" />




<img width="1509" height="819" alt="resim" src="https://github.com/user-attachments/assets/1fd22ce8-3853-45e2-b2f9-c5247d674663" />


<img width="1509" height="819" alt="resim" src="https://github.com/user-attachments/assets/7dcc305d-dbb5-43c9-a598-b8b8f7cbdad7" />


---

## 🛠️ Vulnerability Modules

### 1. Web Application Attacks

The platform includes dedicated modules for practicing common web exploits:

* **SQL Injection (SQLi):** Database manipulation through login forms.
* **XML External Entity (XXE):** Exploiting XML parsers to read sensitive system files like `/etc/passwd`.
* **Insecure Direct Object Reference (IDOR):** Accessing unauthorized user profiles via ID manipulation.
* **Local File Inclusion (LFI) & Log Poisoning:** Including system files or poisoning Apache logs to achieve RCE.
* **Unrestricted File Upload:** Bypassing filters to upload web shells.
* **Remote Code Execution (RCE):** A direct system command console.

### 2. Infrastructure & Post-Exploitation

The lab simulates a deep internal network environment:

* **Service Exploitation:** Anonymous FTP access, writable SMB shares, and unprotected Redis instances.
* **Privilege Escalation:**
* **SUID Binaries:** Exploiting the `find` command with SUID bits set.
* **Wildcard Cronjobs:** Exploiting a backup script using `tar` wildcards.


* **Information Leakage:** Exposed `.env` files containing administrative secrets.

---

## 📦 Deployment & Usage

### Prerequisites

* Python 3.x
* Docker (installed and running)

### Instructions

Simply run the simulation script to build and launch the fortress:

```bash
python3 HeJoTarget.py

```

Upon execution, the script automatically generates the necessary PHP files, Dockerfiles, and service configurations, then launches the container.

---

## 🌐 Target Access Information

Once the system is live, the following ports are mapped to your localhost:

| Service | Local Port | Credentials / Notes |
| --- | --- | --- |
| **HTTP (Web)** | 80 | http://localhost |
| **SSH** | 2222 | `hejo-user` : `password123` |
| **FTP** | 21 | Anonymous Upload Enabled |
| **SMB** | 445 | Writable "Public" Share |
| **Redis** | 6379 | No Password / Protected Mode Off |

---

## ⚠️ Disclaimer

This project is for **educational and ethical hacking purposes only**. The environment is intentionally vulnerable. Ensure you only run this in a controlled environment. The script includes a cleanup routine that removes the Docker container and image upon exiting the interactive shell.
