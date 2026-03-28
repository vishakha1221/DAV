from __future__ import annotations

from pathlib import Path
from typing import Any

import joblib
from flask import Flask, jsonify, request, send_from_directory

from preprocess import preprocess_record


PROJECT_ROOT = Path(__file__).resolve().parent.parent
FRONTEND_DIR = PROJECT_ROOT / "frontend"
MODEL_PATH = PROJECT_ROOT / "model" / "model.pkl"


def create_app() -> Flask:
    app = Flask(__name__)

    model_cache: dict[str, Any] = {"model": None}

    @app.after_request
    def add_cors_headers(response: Any) -> Any:
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        return response

    def load_model() -> Any:
        if model_cache["model"] is None:
            if not MODEL_PATH.exists():
                raise FileNotFoundError(
                    f"Model not found at {MODEL_PATH}. Run notebook/model_training.ipynb first to create model.pkl."
                )
            model_cache["model"] = joblib.load(MODEL_PATH)
        return model_cache["model"]

    @app.get("/")
    def index() -> Any:
        return send_from_directory(FRONTEND_DIR, "index.html")

    @app.get("/<path:filename>")
    def frontend_assets(filename: str) -> Any:
        asset_path = FRONTEND_DIR / filename
        if not asset_path.exists() or not asset_path.is_file():
            return jsonify({"error": "File not found."}), 404
        return send_from_directory(FRONTEND_DIR, filename)

    @app.get("/health")
    def health() -> Any:
        return jsonify({"status": "ok"})

    @app.post("/predict")
    def predict() -> Any:
        try:
            payload = request.get_json(silent=True) or {}
            if not isinstance(payload, dict):
                return jsonify({"error": "Request body must be a JSON object."}), 400

            features = preprocess_record(payload)
            model = load_model()
            prediction = model.predict(features)[0]
            return jsonify({"prediction": str(prediction)})
        except ValueError as exc:
            return jsonify({"error": str(exc)}), 400
        except FileNotFoundError as exc:
            return jsonify({"error": str(exc)}), 500
        except Exception as exc:  # pragma: no cover - defensive API guard
            return jsonify({"error": f"Prediction failed: {exc}"}), 500

    return app


if __name__ == "__main__":
    application = create_app()
    application.run(host="0.0.0.0", port=5000, debug=True)
