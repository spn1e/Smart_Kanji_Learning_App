import cv2
import pytesseract
from sudachipy import dictionary, tokenizer
import random

# Tesseract & Sudachi setup
pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
tokenizer_obj = dictionary.Dictionary().create()
split_mode = tokenizer.Tokenizer.SplitMode.C

def extract_kanji_from_image(image_path: str) -> str:
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return pytesseract.image_to_string(gray, lang='jpn').strip()

def get_readings(text: str) -> list[dict]:
    results = []
    for m in tokenizer_obj.tokenize(text, split_mode):
        results.append({
            'surface': m.surface(),
            'reading': m.reading_form()
        })
    return results

def create_quiz_from_readings(readings: list[dict]) -> dict:
    item = random.choice(readings)
    correct = item['reading']
    distractors = [r['reading'] for r in readings if r['reading'] != correct]
    options = random.sample(distractors, min(3, len(distractors))) + [correct]
    random.shuffle(options)
    return {
        'question': f"Reading for “{item['surface']}”?",
        'options': options,
        'answer': correct
    }
