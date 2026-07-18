# 🛡️ Projeto Sentinela

> **Guardião Digital Local-First:** Um ecossistema de proteção parental descentralizado e privado, rodando em Edge Computing para blindar crianças e adolescentes contra predadores online, sem expor os dados familiares à nuvem.

O **Projeto Sentinela** nasceu da urgência em fechar lacunas de segurança digital ignoradas pelas grandes plataformas. Utilizando IA em hardware doméstico, rede mesh e inteligência de fontes abertas (OSINT), o sistema cria um perímetro de defesa em tempo real, focado na privacidade absoluta (Zero-Cloud).

---

## ⚙️ Arquitetura do Sistema

O ecossistema foi desenhado para operar com alta eficiência em hardwares com restrição de memória (otimizado para servidores Linux com 8GB de RAM), dividido em 4 pilares técnicos:

1. **Inteligência e Semântica (n8n + Ollama):** Interceptação de mensagens de números desconhecidos via APIs (WAHA/Evolution). O payload é analisado por LLMs locais (ex: Gemma 2B) que buscam padrões comportamentais de aliciamento e códigos visuais suspeitos.
2. **Cerca Elétrica e DNS (Tailscale + AdGuard Home):** Rede SD-WAN forçando o roteamento do celular protegido para o servidor doméstico, barrando sites sem moderação, plataformas de apostas e links maliciosos de forma cirúrgica.
3. **Módulo Tático Android (Background Services):** Aplicativo protegido por permissões de *Device Administrator* (bloqueio de desinstalação via TOTP). Conta com geofencing (Fórmula de Haversine) e um gatilho oculto (SOS via botões de hardware) para telemetria de emergência.
4. **Motor de Background Check (PostgreSQL + Python):** Scripts de ETL que cruzam as interações de contatos suspeitos com uma base de dados local focada em antecedentes de domínio público, emitindo alertas privados criptografados.

---

## 🛠️ Stack Tecnológica

* **Orquestração de Fluxos:** n8n (Self-hosted via Docker)
* **Inteligência Artificial:** Ollama (LLMs Nano/Micro)
* **Segurança e Rede:** Tailscale (WireGuard) / AdGuard Home
* **Backend & API:** Python / FastAPI
* **Banco de Dados:** PostgreSQL / SQLite
* **Integração de Mensageria:** WAHA / Evolution API

---

## 📂 Estrutura do Repositório (Mono-repo)

- `/backend` - APIs em FastAPI, scripts de ETL (Web Scraping) e lógica de Geofencing.
- `/mobile` - Código fonte do cliente Android (sensores e anti-tampering).
- `/infra` - Arquivos `docker-compose.yml` e configurações de ambiente (AdGuard, Ollama, n8n).
- `/docs` - Documentação de arquitetura, manuais e referências de cibersegurança.

---

## 🚀 Como Contribuir (Para a Equipe)

Este projeto está sendo construído em módulos para facilitar o desenvolvimento paralelo. Se você faz parte da equipe, verifique as *Issues* para ver qual módulo estamos atacando na sprint atual. 

**Regra de Ouro:** Nenhum dado sensível ou *token* de API deve ser comitado. Usem os arquivos `.env` baseados no `.env.example`.

*Criado para fazer a diferença.*