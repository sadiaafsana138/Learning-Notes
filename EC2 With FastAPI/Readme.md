# EC2 FastAPI Hosting — Cheatsheet

> Ubuntu 22.04 LTS · Copy-paste ready commands

---

## 1. SSH into EC2

```bash
# Set key permission (do this once)
chmod 400 your-key.pem

# Connect
ssh -i "your-key.pem" ubuntu@<EC2-DNS>
```

> Get EC2 DNS from AWS Console → EC2 → Instances → Public IPv4 DNS

---

## 2. Install Dependencies

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git nginx -y
```

---

## 3. Clone & Setup

```bash
cd ~
git clone https://github.com/USER/REPO.git
cd REPO

# Create virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 4. Test Run

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

> Visit `http://<EC2-IP>:8000/docs` to verify. Press `Ctrl+C` to stop.

---

## 5. Systemd Service (auto-start on reboot)

```bash
sudo nano /etc/systemd/system/myapp.service
```

Paste this content:

```ini
[Unit]
Description=My FastAPI App
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/REPO
ExecStart=/home/ubuntu/REPO/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Save: `Ctrl+X` → `Y` → `Enter`

```bash
sudo systemctl daemon-reload
sudo systemctl enable myapp
sudo systemctl start myapp
```

---

## 6. Nginx Setup (reverse proxy)

```bash
sudo nano /etc/nginx/sites-available/myapp
```

Paste this content:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

> Replace `yourdomain.com` with your actual domain or EC2 IP.

```bash
sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
sudo nginx -t        # Should print "test is successful"
sudo systemctl restart nginx
```

---

## 7. SSL Certificate (free, auto-renews)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d yourdomain.com
```

---

## 8. DNS — A Record

Set this in Route53 or any DNS provider:

```
Type  : A
Name  : @ (root) or subdomain
Value : <EC2 Public IP>
TTL   : 300
```

---

## Deploy — Code Update

**On your local machine:**
```bash
git add .
git commit -m "message"
git push
```

**On EC2:**
```bash
cd ~/REPO && git pull
sudo service myapp restart
```

---

## Useful Commands

| Command | Purpose |
|---|---|
| `sudo service myapp status` | Check if app is running |
| `sudo journalctl -u myapp -f` | Live logs |
| `sudo service myapp restart` | Restart app |
| `sudo systemctl restart nginx` | Restart Nginx |
| `sudo nginx -t` | Validate Nginx config |
