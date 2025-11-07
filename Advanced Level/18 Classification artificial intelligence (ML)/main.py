import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def preprocess(data):
    # Örnek: Son sütun hedef sınıf
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    
    # Kategorik verileri etiketleyici ile sayısala çevir
    le = LabelEncoder()
    for col in X.select_dtypes(include=['object']).columns:
        X[col] = le.fit_transform(X[col])
    y = le.fit_transform(y)
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train, y_train):
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    return clf

def evaluate_model(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    print("Doğruluk Oranı:", accuracy_score(y_test, y_pred))
    print("Sınıflandırma Raporu:\n", classification_report(y_test, y_pred))

def main():
    print("Sınıflandırma Yapay Zekası Projesi")
    data = load_data('data/dataset.csv')
    X_train, X_test, y_train, y_test = preprocess(data)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()
