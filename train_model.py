import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Устанавливаем seed для повторяемости
np.random.seed(42)

# Количество "матчей" для обучения
num_matches = 500

# Генерация фейковых данных
data = pd.DataFrame({
    'xG_home': np.random.uniform(0.5, 3.5, num_matches),
    'xG_away': np.random.uniform(0.2, 2.5, num_matches),
    'form_home': np.random.uniform(0, 1, num_matches),
    'form_away': np.random.uniform(0, 1, num_matches),
    'home_goals': np.random.poisson(1.8, num_matches),
    'away_goals': np.random.poisson(1.2, num_matches),
})

# Фичи и цели
X = data[['xG_home', 'xG_away', 'form_home', 'form_away']]
y_home = data['home_goals']
y_away = data['away_goals']

# Модель для голов хозяев
model_home = LinearRegression()
model_home.fit(X, y_home)

# Модель для голов гостей
model_away = LinearRegression()
model_away.fit(X, y_away)

# Сохраняем модели
joblib.dump(model_home, 'home_model.pkl')
joblib.dump(model_away, 'away_model.pkl')

print("✅ Модели обучены и сохранены: home_model.pkl, away_model.pkl")
