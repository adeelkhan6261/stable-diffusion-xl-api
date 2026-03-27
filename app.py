"""
SDXL Web Interface — Flask backend
Run:  python app.py
Then open http://localhost:5000 in your browser.
"""

from flask import Flask, render_template, request, jsonify
from sdxl import ImageGenerator

app = Flask(__name__)
generator = ImageGenerator()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json(force=True)

    prompt = (data.get("prompt") or "").strip()
    if not prompt:
        return jsonify({"error": "Prompt cannot be empty."}), 400

    try:
        count            = int(data.get("count", 1))
        width            = int(data.get("width", 1024))
        height           = int(data.get("height", 1024))
        scheduler        = data.get("scheduler", "DDIM")
        guidance_scale   = float(data.get("guidance_scale", 7.5))
        high_noise_frac  = float(data.get("high_noise_frac", 0.8))
        prompt_strength  = float(data.get("prompt_strength", 0.8))
        num_steps        = int(data.get("num_inference_steps", 50))
    except (ValueError, TypeError) as e:
        return jsonify({"error": f"Invalid parameter: {e}"}), 400

    result = generator.gen_image(
        prompt=prompt,
        count=count,
        width=width,
        height=height,
        scheduler=scheduler,
        guidance_scale=guidance_scale,
        high_noise_frac=high_noise_frac,
        prompt_strength=prompt_strength,
        num_inference_steps=num_steps,
    )

    if result is None:
        return jsonify({"error": "Image generation failed. Check your parameters and try again."}), 500

    return jsonify(result)


if __name__ == "__main__":
    print("🎨 SDXL Web UI running at http://localhost:5000")
    app.run(debug=True, port=5000)
