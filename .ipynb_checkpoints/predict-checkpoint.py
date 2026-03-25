import os
import pickle
import pandas as pd
from text_cleaner import wordopt

class FakeNewsPredictor:
    def __init__(self, model_dir='models', data_dir='.'):
        # Load vectorizer and trained models
        self.vectorizer = self._load_model(os.path.join(model_dir, "vectorizer.pkl"))
        self.lr_model = self._load_model(os.path.join(model_dir, "model_LR.pkl"))
        self.rf_model = self._load_model(os.path.join(model_dir, "model_RF.pkl"))

        # Load training CSVs to create a recognition set
        fake_df = pd.read_csv(os.path.join(data_dir, "Fake.csv"))
        true_df = pd.read_csv(os.path.join(data_dir, "True.csv"))
        all_data = pd.concat([fake_df, true_df], ignore_index=True)
        all_data["text_cleaned"] = all_data["text"].apply(wordopt)
        self.recognized_set = set(all_data["text_cleaned"].tolist())

    def _load_model(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"Model file not found: {path}")
        with open(path, "rb") as f:
            return pickle.load(f)

    def debug_closest_matches(self, cleaned_input):
        # Optional: prints similar texts from training data
        for item in self.recognized_set:
            if cleaned_input[:30] in item or item[:30] in cleaned_input:
                print("💡 Close Match Found:")
                print("Input:", cleaned_input[:100])
                print("Training Data:", item[:100])
                print("Match Score (chars in common):", len(set(cleaned_input) & set(item)))

    def predict(self, news_text):
        if not news_text.strip():
            return {'Status': 'EmptyInput'}

        cleaned_input = wordopt(news_text)
        vectorized = self.vectorizer.transform([cleaned_input])
        lr_pred = self.lr_model.predict(vectorized)[0]
        rf_pred = self.rf_model.predict(vectorized)[0]

        is_recognized = cleaned_input in self.recognized_set
        if not is_recognized:
            self.debug_closest_matches(cleaned_input)

        predictions = {
            'Logistic Regression': 'Not Fake News' if lr_pred == 1 else 'Fake News',
            'Random Forest': 'Not Fake News' if rf_pred == 1 else 'Fake News',
            'Status': 'Known' if is_recognized else 'Unrecognized'
        }

        return predictions
