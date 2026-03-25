# config.py

# === File Paths ===
MODEL_DIR = 'models'
DATA_DIR = 'data'

# === Training Settings ===
TFIDF_MAX_DF = 0.7
TFIDF_STOPWORDS = 'english'

# === UI Settings ===
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 500
FONT_HEADER = ("Helvetica", 20, "bold")
FONT_TEXT = ("Arial", 13)
FONT_INPUT = ("Arial", 12)
FONT_OUTPUT = ("Arial", 14)

COLOR_PRIMARY = "#005f73"
COLOR_BUTTON = "#0a9396"
COLOR_BG = "#f0f4f7"
COLOR_SUCCESS = "green"
COLOR_WARNING = "orange"
COLOR_ERROR = "red"

# === Custom Messages ===
MSG_EMPTY = "⚠️ Please enter some news content."
MSG_UNKNOWN = "⚠️ This news is not recognized. It might be new or unverified.\nPlease try a different article."
MSG_REAL = "✅ This news seems to be Real and Trustworthy."
MSG_FAKE = "🚨 This news appears to be Fake or Misleading."

MODEL_DIR = 'models'
DATA_DIR = 'data'
