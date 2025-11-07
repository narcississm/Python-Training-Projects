import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['target'] = iris.target
    return df, iris.target_names

def train_model(df):
    X = df.iloc[:, :-1]
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model doğruluk oranı: {accuracy:.2f}")
    return model

def predict_sample(model, target_names):
    print("\nYeni veri tahmini için çiçek özelliklerini giriniz:")
    sepal_length = float(input("Çanak yaprak uzunluğu (cm): "))
    sepal_width = float(input("Çanak yaprak genişliği (cm): "))
    petal_length = float(input("Taç yaprak uzunluğu (cm): "))
    petal_width = float(input("Taç yaprak genişliği (cm): "))
    
    sample = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(sample)[0]
    print(f"Tahmin edilen çiçek türü: {target_names[prediction]}")

def main():
    df, target_names = load_data()
    model = train_model(df)
    while True:
        predict_sample(model, target_names)
        cont = input("Devam etmek ister misiniz? (e/h): ").lower()
        if cont != 'e':
            print("Program sonlandırılıyor.")
            break

if __name__ == "__main__":
    main()
