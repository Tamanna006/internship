
import os
import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from text_cleaner import wordopt  # make sure this file is in same folder

class FakeNewsTrainer:
    def __init__(self, data_dir='.', model_dir='models'):
        self.data_dir = data_dir
        self.model_dir = model_dir
        os.makedirs(self.model_dir, exist_ok=True)

    def load_and_clean_data(self):
        # Load CSVs from current folder
        data_fake = pd.read_csv(os.path.join(self.data_dir, 'Fake.csv'))
        data_true = pd.read_csv(os.path.join(self.data_dir, 'True.csv'))

        # Add class labels
        data_fake['class'] = 0
        data_true['class'] = 1

        # Combine datasets
        data = pd.concat([data_fake, data_true], ignore_index=True)
        data['text'] = data['text'].apply(wordopt)

        return data['text'], data['class']

    def vectorize_text(self, texts):
        vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
        xv = vectorizer.fit_transform(texts)

        path = os.path.join(self.model_dir, 'vectorizer.pkl')
        with open(path, 'wb') as f:
            pickle.dump(vectorizer, f)
        print("✅ Vectorizer saved.")
        return vectorizer, xv

    def train_and_save(self, model, name, xv, y):
        model.fit(xv, y)
        with open(os.path.join(self.model_dir, f"{name}.pkl"), 'wb') as f:
            pickle.dump(model, f)
        print(f"✅ {name} model saved.")

    def run(self):
        print("📦 Loading data...")
        x, y = self.load_and_clean_data()

        print("🧠 Vectorizing...")
        vectorizer, xv = self.vectorize_text(x)

        print("🚀 Training models...")
        self.train_and_save(LogisticRegression(max_iter=1000), "model_LR", xv, y)
        self.train_and_save(RandomForestClassifier(), "model_RF", xv, y)

# For Jupyter, you can run this directly
if __name__ == "__main__":
    trainer = FakeNewsTrainer()
    trainer.run()
