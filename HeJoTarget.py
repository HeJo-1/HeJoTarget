#!/usr/bin/env python3
import os
import subprocess
import sys
import time
from pathlib import Path

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    PURPLE = '\033[35m'

class HeJoTarget:
    def __init__(self):
        self.container_name = "hejotarget"
        self.image_name = "hejo_ultimate"
        self.temp_files = [
            "index.php", "style.css", "labs.php", "info.php",
            "sqli.php", "upload.php", "cmd.php", "ssrf.php",
            "xxe.php", "idor.php", "lfi.php", ".env",
            "Dockerfile", "vsftpd.conf", "start.sh", "smb.conf"
        ]

    def print_banner(self):
        banner = f"""
{Colors.PURPLE}

     {Colors.BOLD}██╗  ██╗███████╗     ██╗ ██████╗ ████████╗ █████╗ ██████╗  ██████╗ ███████╗████████╗{Colors.END}{Colors.PURPLE}
     {Colors.BOLD}██║  ██║██╔════╝     ██║██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔════╝ ██╔════╝╚══██╔══╝{Colors.END}{Colors.PURPLE}
     {Colors.BOLD}███████║█████╗       ██║██║   ██║   ██║   ███████║██████╔╝██║  ███╗█████╗     ██║   {Colors.END}{Colors.PURPLE}
     {Colors.BOLD}██╔══██║██╔══╝  ██   ██║██║   ██║   ██║   ██╔══██║██╔══██╗██║   ██║██╔══╝     ██║   {Colors.END}{Colors.PURPLE}
     {Colors.BOLD}██║  ██║███████╗╚█████╔╝╚██████╔╝   ██║   ██║  ██║██║  ██║╚██████╔╝███████╗   ██║   {Colors.END}{Colors.PURPLE}
     {Colors.BOLD}╚═╝  ╚═╝╚══════╝ ╚════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   {Colors.END}{Colors.PURPLE}

              Advanced Penetration Testing Training Platform
                  Full-Stack Infrastructure Lab

{Colors.CYAN}[*] Integrated: Web, SSH, SMB, FTP, Redis, PrivEsc, Log Poisoning{Colors.END}
{Colors.GREEN}[+] Initializing Deployment...{Colors.END}
"""
        print(banner)

    def generate_php_page(self, title, content):
        return f"""<?php error_reporting(0); session_start(); ?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title} - HeJoTarget</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="glass-card">
        {content}
        <div class="nav-footer">
            <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.1); margin: 20px 0;">
            <a href="index.php">Main Menu</a> | <a href="labs.php">Modules</a> | <a href="info.php">Target Info</a>
        </div>
    </div>
</body>
</html>"""

    def create_web_assets(self):
        style_css = """
        body {
            margin: 0; padding: 0; min-height: 100vh;
            display: flex; justify-content: center; align-items: center;
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            font-family: 'Segoe UI', sans-serif; color: white;
        }
        .glass-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px); -webkit-backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px; padding: 40px; text-align: center;
            box-shadow: 0 15px 35px rgba(0,0,0,0.5); width: 90%; max-width: 900px;
        }
        .btn-main {
            background: #00d2ff; color: #000; padding: 10px 25px; border-radius: 5px;
            text-decoration: none; font-weight: bold; display: inline-block; margin: 5px; border: none; cursor: pointer;
        }
        .btn-main:hover { background: #fff; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 20px 0; }
        .lab-box { background: rgba(0,0,0,0.3); padding: 15px; border-radius: 10px; border: 1px solid rgba(0,210,255,0.2); transition: 0.3s; }
        .lab-box:hover { border-color: #00d2ff; }
        input, textarea { width: 100%; padding: 10px; margin: 10px 0; border-radius: 5px; border: 1px solid #333; background: #111; color: #0f0; box-sizing: border-box; }
        pre { background: #000; color: #0f0; padding: 15px; border-radius: 5px; text-align: left; overflow: auto; border: 1px solid #333; }
        .nav-footer a { color: #00d2ff; text-decoration: none; font-size: 0.8rem; margin: 0 10px; }
        """

        index_content = """
            <h1>HeJo Target</h1>
            <p style="opacity:0.7;">Full Spectrum Vulnerability Lab</p>
            <div class="grid">
                <div class="lab-box"><h3>Web Attacks</h3><p style="font-size:0.7rem">SQLi, LFI, XXE, IDOR</p><a href="labs.php" class="btn-main">Launch</a></div>
                <div class="lab-box"><h3>Infrastructure</h3><p style="font-size:0.7rem">SSH, FTP, SMB, Redis</p></div>
                <div class="lab-box"><h3>Post-Exploitation</h3><p style="font-size:0.7rem">SUID, Cron, Log Poisoning</p></div>
            </div>
        """

        xxe_content = """
            <h2>XXE - XML External Entity</h2>
            <p>Objective: Read /etc/passwd via XML injection.</p>
            <form method="POST">
                <textarea name="xml" rows="5" placeholder='<?xml version="1.0"?><!DOCTYPE root [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><root>&xxe;</root>'></textarea>
                <input type="submit" class="btn-main" value="Process XML">
            </form>
            <?php
            if(isset($_POST['xml'])){
                libxml_disable_entity_loader(false);
                $xml = simplexml_load_string($_POST['xml'], 'SimpleXMLElement', LIBXML_NOENT);
                echo "<pre>Output: " . htmlspecialchars($xml) . "</pre>";
            }
            ?>
        """

        lfi_content = """
            <h2>LFI & Log Poisoning</h2>
            <p>Try to include system files or poison logs.</p>
            <form method="GET">
                <input name="page" placeholder="example: info.php">
                <input type="submit" class="btn-main" value="Load Page">
            </form>
            <?php
            if(isset($_GET['page'])){
                $file = $_GET['page'];
                include($file);
            }
            ?>
        """

        idor_content = """
            <h2>Insecure Direct Object Reference</h2>
            <p>Target Profile ID: <b>2</b></p>
            <?php
            $id = $_GET['id'] ?? 2;
            $db = new SQLite3('/var/www/db/lab.db');
            $user = $db->querySingle("SELECT * FROM users WHERE id=$id", true);
            if($user){
                echo "<div class='lab-box'><h3>User: ".htmlspecialchars($user['user'])."</h3><p>Secret Note: ".htmlspecialchars($user['bio'])."</p></div>";
            } else { echo "Profile not found."; }
            ?>
        """

        with open("style.css", "w") as f: f.write(style_css)
        with open("index.php", "w") as f: f.write(self.generate_php_page("Home", index_content))
        with open("xxe.php", "w") as f: f.write(self.generate_php_page("XXE Module", xxe_content))
        with open("lfi.php", "w") as f: f.write(self.generate_php_page("LFI Module", lfi_content))
        with open("idor.php", "w") as f: f.write(self.generate_php_page("IDOR Module", idor_content))
        with open(".env", "w") as f: f.write("ADMIN_SECRET=HEJO{ENVIRONMENT_EXPOSURE_2024}\nDATABASE_PASS=v19_secret_db_pass\nBACKUP_KEY=infra_key_99")

        labs_content = """
            <h2>Attack Modules</h2>
            <div class="grid">
                <div class="lab-box"><a href="sqli.php" style="color:#00d2ff">SQL Injection</a></div>
                <div class="lab-box"><a href="xxe.php" style="color:#00d2ff">XXE (XML)</a></div>
                <div class="lab-box"><a href="idor.php?id=2" style="color:#00d2ff">IDOR</a></div>
                <div class="lab-box"><a href="lfi.php?page=info.php" style="color:#00d2ff">LFI / Logs</a></div>
                <div class="lab-box"><a href="upload.php" style="color:#00d2ff">Shell Upload</a></div>
                <div class="lab-box"><a href="cmd.php" style="color:#00d2ff">RCE Console</a></div>
            </div>
        """
        with open("labs.php", "w") as f: f.write(self.generate_php_page("Modules", labs_content))
        with open("sqli.php", "w") as f: f.write(self.generate_php_page("SQLi", '<h2>SQL Injection</h2><form method="POST"><input name="u" placeholder="Username"><input name="p" type="password" placeholder="Password"><input type="submit" class="btn-main"></form>'))
        with open("upload.php", "w") as f: f.write(self.generate_php_page("File Upload", '<h2>Unrestricted Upload</h2><form method="POST" enctype="multipart/form-data"><input type="file" name="f"><input type="submit" class="btn-main" value="Upload Shell"></form>'))
        with open("cmd.php", "w") as f: f.write(self.generate_php_page("Command Execution", '<h2>System Command RCE</h2><form method="POST"><input name="c" placeholder="whoami"><input type="submit" class="btn-main" value="Execute"></form>'))
        with open("info.php", "w") as f: f.write(self.generate_php_page("Info", '<h2>Lab Overview</h2><p>Infrastructure: SSH(22), FTP(21), SMB(445), Redis(6379), Web(80)<br>System: SUID Find, Wildcard Cron, World-Writable Files</p>'))

    def create_configs(self):
        with open("vsftpd.conf", "w") as f:
            f.write("listen=YES\nanonymous_enable=YES\nwrite_enable=YES\nanon_upload_enable=YES\nanon_root=/var/www/html/uploads\nseccomp_sandbox=NO\n")

        with open("smb.conf", "w") as f:
            f.write("[global]\nworkgroup = WORKGROUP\nserver string = Samba Server\nsecurity = user\nmap to guest = Bad User\n\n[public]\npath = /var/www/html/uploads\nbrowsable = yes\nwritable = yes\nguest ok = yes\nread only = no\n")

        with open("start.sh", "w") as f:
            f.write("#!/bin/bash\n"
                    "useradd -m hejo-user && echo 'hejo-user:password123' | chpasswd\n"
                    "mkdir -p /var/run/vsftpd/empty /var/www/db /var/www/html/uploads /var/backups/html /var/run/sshd\n"
                    "sqlite3 /var/www/db/lab.db 'CREATE TABLE users(id INT, user TEXT, pass TEXT, bio TEXT); INSERT INTO users VALUES(1, \"admin\", \"complex_pass_998\", \"FLAG: HEJO{IDOR_INFRA_OWNER}\"); INSERT INTO users VALUES(2, \"guest\", \"guest\", \"Standard guest account.\");'\n"
                    "chown -R www-data:www-data /var/www/db /var/www/html/uploads /var/log/apache2\n"
                    "chmod 777 /var/www/html/uploads /var/backups/html /var/log/apache2\n"
                    "chmod u+s /usr/bin/find\n"
                    "echo 'cd /var/www/html/uploads && tar -cf /var/backups/html/backup.tar *' > /usr/local/bin/backup.sh\n"
                    "chmod +x /usr/local/bin/backup.sh\n"
                    "echo '* * * * * root /usr/local/bin/backup.sh' > /etc/cron.d/backup-job\n"
                    "sed -i 's/bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf\n"
                    "sed -i 's/protected-mode yes/protected-mode no/' /etc/redis/redis.conf\n"
                    "service ssh start\n"
                    "service smbd start\n"
                    "service redis-server start\n"
                    "cron && vsftpd /etc/vsftpd.conf &\n"
                    "apache2-foreground")

        with open("Dockerfile", "w") as f:
            f.write("FROM php:7.4-apache\n"
                    "RUN apt-get update && apt-get install -y vsftpd sqlite3 sudo cron openssh-server samba redis-server\n"
                    "COPY . /var/www/html/\n"
                    "COPY vsftpd.conf /etc/vsftpd.conf\n"
                    "COPY smb.conf /etc/samba/smb.conf\n"
                    "COPY start.sh /start.sh\n"
                    "RUN chmod +x /start.sh\n"
                    "EXPOSE 80 21 22 445 6379\n"
                    "ENTRYPOINT [\"/start.sh\"]")

    def interactive_shell(self):
        print(f"\n{Colors.PURPLE}{Colors.BOLD}>>> HEJO COMMAND CENTER <<<")
        self.print_banner()
        print(f"{Colors.CYAN}Target Ports: 80(HTTP), 22(SSH), 21(FTP), 445(SMB), 6379(Redis)")
        print(f"\n{Colors.GREEN}{Colors.BOLD}SYSTEM LIVE: http://localhost{Colors.END}")
        print(f"{Colors.CYAN}SSH Access: ssh hejo-user@localhost -p 2222 (pass: password123){Colors.END}")
        while True:
            try:
                cmd = input(f"{Colors.GREEN}HeJo-Target# {Colors.END}")
                if cmd.lower() in ["exit", "quit"]: break
                if not cmd.strip(): continue
                subprocess.run(["docker", "exec", "-it", self.container_name, "bash", "-c", cmd])
            except KeyboardInterrupt: break

    def cleanup(self):
        print(f"\n{Colors.WARNING}[!] Decommissioning Fortress...{Colors.END}")
        subprocess.run(["docker", "rm", "-f", self.container_name], stderr=subprocess.DEVNULL)
        subprocess.run(["docker", "rmi", self.image_name], stderr=subprocess.DEVNULL)
        for f in self.temp_files:
            if os.path.exists(f): os.remove(f)
        print(f"{Colors.GREEN}[✓] All traces removed successfully.{Colors.END}")

    def run(self):
        self.print_banner()
        try:
            self.create_web_assets()
            self.create_configs()
            print(f"{Colors.BLUE}[*] Building Infrastructure...{Colors.END}")
            subprocess.run(["docker", "build", "-t", self.image_name, "."], check=True)
            print(f"{Colors.BLUE}[*] Launching Services...{Colors.END}")
            subprocess.run(["docker", "run", "-d", "--name", self.container_name,
                            "-p", "80:80", "-p", "21:21", "-p", "2222:22",
                            "-p", "445:445", "-p", "6379:6379", self.image_name], check=True)
            
            self.interactive_shell()
        except Exception as e:
            print(f"{Colors.FAIL}Error: {e}{Colors.END}")
        finally:
            self.cleanup()

if __name__ == "__main__":
    lab = HeJoTarget()
    lab.run()
