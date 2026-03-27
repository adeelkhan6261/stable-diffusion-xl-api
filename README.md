![Banner](assets/banner.png)
# SDXL Studio — Stable Diffusion XL API

> A Python wrapper & web UI for generating stunning AI images via Stable Diffusion XL — no API key required.

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web%20UI-black?style=flat-square&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![GitHub](https://img.shields.io/badge/GitHub-adeelkhan6261-181717?style=flat-square&logo=github)

---

## ✨ Features

- **Text-to-Image** — generate 1–4 images from any text prompt
- **Web UI** — beautiful dark-themed browser interface (no terminal needed)
- **CLI** — command-line usage for scripting & automation
- **Advanced Controls** — scheduler, guidance scale, inference steps, noise frac & more
- **Python Library** — import and use in your own projects

---

## 📋 Requirements

- Python **3.8+**
- pip

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/adeelkhan6261/stable-diffusion-xl-api.git
cd stable-diffusion-xl-api
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Web UI

```bash
python app.py
```

Then open **http://localhost:5000** in your browser. That's it! 🎉

---

## 🖥️ Web UI

The web interface lets you:
- Type your prompt
- Choose number of images (1–4), size, and scheduler
- Adjust advanced settings (guidance scale, inference steps, etc.)
- View and open generated images directly

---

## 💻 CLI Usage

```bash
# Basic usage
python example/cli.py "A futuristic city at sunset, ultra realistic"

# With options
python example/cli.py "A dragon flying over mountains" \
  --count 2 \
  --scheduler K_EULER \
  --guidance_scale 8.0 \
  --num_inference_steps 60
```

### CLI Options

| Flag | Default | Description |
|------|---------|-------------|
| `--count` | 1 | Number of images (1–4) |
| `--width` | 1024 | Image width in pixels |
| `--height` | 1024 | Image height in pixels |
| `--scheduler` | DDIM | Sampling scheduler |
| `--guidance_scale` | 7.5 | How closely to follow the prompt (1–50) |
| `--high_noise_frac` | 0.8 | High noise fraction (0–1) |
| `--prompt_strength` | 0.8 | Prompt strength (0–1) |
| `--num_inference_steps` | 50 | Quality / speed tradeoff (1–500) |

---

## 🐍 Python Library Usage

```python
from sdxl import ImageGenerator

client = ImageGenerator()

result = client.gen_image(
    prompt="A futuristic city at sunset, ultra realistic, cinematic lighting",
    count=2,
    scheduler="K_EULER",
    guidance_scale=8.0,
    num_inference_steps=60
)

print(result)
# {'prompt': '...', 'images': ['https://...', 'https://...']}
```

---

## 📁 Project Structure

```
stable-diffusion-xl-api/
├── app.py                 # Flask web server
├── requirements.txt       # Dependencies
├── setup.py               # Package setup
├── sdxl/
│   ├── __init__.py
│   └── sdxl.py            # ImageGenerator class
├── example/
│   └── cli.py             # Command-line interface
└── templates/
    └── index.html         # Web UI
```

---

## ⚙️ Available Schedulers

| Scheduler | Notes |
|-----------|-------|
| `DDIM` | Fast, deterministic — good default |
| `DPMSolverMultistep` | High quality, fewer steps needed |
| `HeunDiscrete` | High accuracy, slower |
| `KarrasDPM` | Sharp details |
| `K_EULER_ANCESTRAL` | Creative/varied results |
| `K_EULER` | Balanced quality & speed |
| `PNDM` | Stable, smooth outputs |

---

## ⚠️ Disclaimer

This project uses Replicate's public-facing API for Stable Diffusion XL. It is independently maintained and not affiliated with Stability AI or Replicate. Use responsibly and in accordance with their terms of service.

---

## 📜 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

Developed & maintained by **Adeel Ghauri**

🔗 GitHub: [https://github.com/adeelkhan6261](https://github.com/adeelkhan6261)
