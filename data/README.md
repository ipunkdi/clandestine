# Clandestine

**Clandestine** adalah offensive security & cyber intelligence toolkit berbasis CLI.  
Terinspirasi dari [SysBraykr Military & Intelligence Software](https://sysbraykr.com/software),  
project ini dikembangkan untuk riset, edukasi, dan kompetisi keamanan siber.

---

## ✨ Fitur Utama (Planned)
- **OSINT**  
  - Social media scraper (Twitter, Reddit, Telegram)  
  - WHOIS & domain reconnaissance  
  - Dark web crawler (Tor)  

- **Interception**  
  - Packet sniffer (Scapy/pyshark)  
  - MITM (ARP spoofing, proxy injection)  
  - IMSI catcher (simulation/lab)  

- **Monitoring**  
  - Mass scanning (Nmap-style)  
  - Threat intel feeds (MISP, OTX)  
  - ML-based anomaly detection  

- **Exploits**  
  - SQL injection automation  
  - XSS scanner  
  - Buffer overflow PoC  

---

## 📂 Struktur Project
clandestine/
├── .github/                  # CI/CD workflows (GitHub Actions)
│   └── workflows/
│       ├── tests.yml         # Run pytest on push
│       └── releases.yml      # Auto-publish to PyPI
│
├── core/                     # Core utilities
│   ├── utils/                # Shared helpers
│   │   ├── tor.py            # Tor connection manager
│   │   ├── rate_limiter.py   # API call throttling
│   │   └── decorators.py     # @time_execution, @deprecated
│   ├── config/               # Config loader
│   │   └── loader.py         # Pydantic-validated config
│   ├── logging/              # Logging
│   │   └── json_logger.py    # JSON + file rotation
│   ├── exceptions.py         # Custom errors
│   ├── version.py            # Version tracker
│   └── __init__.py           # Core package init
│
├── modules/                  # Main offensive/defensive modules
│   ├── osint/                # OSINT: Open Source Intelligence
│   │   ├── cli.py            # CLI subcommands (clandestine osint ...)
│   │   ├── social_media.py   # Scraper (Twitter, Reddit, Telegram)
│   │   ├── whois_lookup.py   # WHOIS & domain recon
│   │   ├── dark_web.py       # Tor/Darkweb crawler
│   │   └── __init__.py
│   │
│   ├── interception/         # Network interception
│   │   ├── cli.py            # CLI commands
│   │   ├── sniffer.py        # Packet sniffer (Scapy/pyshark)
│   │   ├── mitm.py           # MITM attack (ARP spoofing, proxy)
│   │   ├── imsi_catcher.py   # GSM IMSI catcher (simulasi/lab)
│   │   └── __init__.py
│   │
│   ├── monitoring/           # Network/system monitoring
│   │   ├── cli.py            # CLI commands
│   │   ├── mass_scan.py      # Mass scanning (Nmap-style)
│   │   ├── threat_intel.py   # Integrasi MISP/OTX feed
│   │   ├── anomaly_detector.py # Deteksi anomali (ML/sklearn)
│   │   └── __init__.py
│   │
│   └── exploits/             # Vulnerability exploitation
│       ├── cli.py            # CLI commands
│       ├── sql_injector.py   # SQL Injection automation
│       ├── xss_scanner.py    # XSS scanning
│       ├── buffer_overflow.py # Buffer overflow PoC
│       └── __init__.py
│
├── output/                   # Operational outputs
│   ├── captures/             # PCAPs, screenshots
│   ├── logs/                 # JSON/plaintext logs
│   ├── reports/              # PDF/HTML reports
│   └── artifacts/            # Memory dumps, binaries
│
├── tests/                    # Tests
│   ├── osint/                # Test osint modules
│   ├── exploits/             # Test exploits
│   ├── monitoring/           # Test monitoring
│   └── interception/         # Test interception
│
├── data/                     # Static files
│   ├── wordlists/            # rockyou.txt, etc.
│   ├── payloads/             # reverse_shells.py
│   ├── signatures/           # YARA/Snort rules
│   └── README.md             # Data directory guide
│
├── plugins/                  # Third-party integrations
│   ├── nuclei/               # Nuclei templates
│   ├── metasploit/           # MSF RPC wrapper
│   └── shodan/               # Shodan API integration
│
├── scripts/                  # Setup scripts
│   ├── install_npcap.ps1     # Windows Npcap install
│   └── tor_launcher.sh       # Linux Tor service
│
├── docs/                     # Documentation
│   ├── api.md                # Module references
│   └── setup_guide.md        # Installation guide
│
├── examples/                 # Tutorials
│   ├── osint/                # OSINT walkthroughs
│   └── exploits/             # Exploit examples
│
├── config/                   # Environment configs
│   ├── default.yaml          # Default config
│   ├── dev.yaml              # Dev environment config
│   └── prod.yaml             # Production config
│
└── clandestine.py            # CLI entry point

---

## 🚀 Cara Jalankan
```bash
# Clone repository
git clone https://github.com/ipunkdi/clandestine.git
cd clandestine

# Install dependencies
pip install -r requirements.txt

# Jalankan CLI
python clandestine.py --help

⚠️ Disclaimer

Project ini dibuat untuk tujuan riset & edukasi.
Penggunaan di luar konteks tersebut sepenuhnya adalah tanggung jawab pengguna.

📜 License

Saat ini belum menggunakan lisensi open-source.
Jika ingin berkontribusi, silakan buat issue atau pull request.

