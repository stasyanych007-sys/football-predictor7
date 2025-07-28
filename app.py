from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Загрузка моделей
try:
    home_model = joblib.load("home_model.pkl")
    away_model = joblib.load("away_model.pkl")
except Exception as e:
    print(f"Ошибка при загрузке моделей: {e}")
    home_model = None
    away_model = None

@app.route("/")
def index():
    return "⚽ AI Football Predictor API is running!"

@app.route("/api/predict", methods=["POST"])
def predict_goals():
    data = request.get_json()

    try:
        features = np.array([[data["home_xg"], data["away_xg"], data["home_form"], data["away_form"]]])
        home_pred = home_model.predict(features)[0]
        away_pred = away_model.predict(features)[0]
        total = home_pred + away_pred

        return jsonify({
            "home_goals_pred": round(home_pred, 2),
            "away_goals_pred": round(away_pred, 2),
            "total_goals_pred": round(total, 2)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
