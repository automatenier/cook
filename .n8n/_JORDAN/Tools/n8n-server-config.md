---
tags:
  - automation
---
# N8N Server Configuration & Toolstack

> Your VPS hosting setup, update guide, and troubleshooting reference.

---

## Infrastructure

| Component | Detail |
|---|---|
| **VPS** | Hostinger (Ubuntu 24.04.3 LTS) |
| **Domain** | htsagency.id |
| **N8N URL** | https://n8n.htsagency.id |
| **Stack** | Docker + Docker Compose + Traefik (reverse proxy) |
| **N8N Data** | `/home/node/.n8n` |
| **Docker Compose** | `/root/docker-compose.yml` |

## Traffic Flow

```
Internet → htsagency.id → Traefik (port 80/443, auto SSL) → n8n container (port 5678)
```

---

## Update Guide

### 1. Access VPS
```bash
# Hostinger hPanel → VPS → Browser Terminal
# Or SSH:
ssh root@your-vps-ip
```

### 2. Backup (ALWAYS first)
```bash
cd /root
mkdir -p backups
cp -r /home/node/.n8n backups/n8n-backup-$(date +%Y%m%d-%H%M%S)
```

### 3. Update n8n
```bash
cd /root
docker-compose pull n8n
docker-compose up -d n8n
```

### 4. Verify
```bash
docker-compose ps
docker-compose logs -f n8n
# Test: https://n8n.htsagency.id
```

### Rollback (if something breaks)
```bash
docker-compose stop n8n
rm -rf /home/node/.n8n
cp -r backups/n8n-backup-YYYYMMDD-HHMMSS /home/node/.n8n
chown -R 1000:1000 /home/node/.n8n
docker-compose up -d n8n
```

---

## Key Commands

| Command | What it does |
|---|---|
| `docker-compose ps` | Check what's running |
| `docker-compose logs -f n8n` | View logs |
| `docker-compose restart n8n` | Restart n8n |
| `docker-compose down` | Stop everything |
| `docker-compose up -d` | Start everything |

---

## Rules
1. **ALWAYS use `docker-compose`** — never manual `docker run` (Traefik needs the labels)
2. **ALWAYS backup before updating**
3. **Don't touch Traefik** — it's working, only update n8n
4. **Check release notes** before updating: https://docs.n8n.io/release-notes/

## Troubleshooting

| Problem | Fix |
|---|---|
| 404 after update | Used `docker run` instead of `docker-compose` → stop manual container, use compose |
| Permission errors | `chown -R 1000:1000 /home/node/.n8n && chmod -R 755 /home/node/.n8n` |
| Can't access terminal | https://hpanel.hostinger.com → VPS → Browser Terminal |
| Container restarting | `docker-compose logs n8n` → check error messages |

## Hostinger Access
- Panel: https://hpanel.hostinger.com
- VPS section → Your VPS → Browser Terminal
