import pandas as pd
import re
import spacy
from transformers import BertTokenizer
from langdetect import detect, LangDetectException

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    """Enhanced text cleaning process"""
    if not isinstance(text, str):
        return ""
    unwanted_phrases = [
        "Video player was slow to load content Video content never loaded Ad froze or did not finish loading Video content did not start after ad Audio on ad was too loud Other issues",
    ]
    for phrase in unwanted_phrases:
        text = text.replace(phrase, "")
    text = re.sub(r'1\. How relevant is this ad to you\?.*\n?', '', text)
    return text

def is_english(text):
    """Determines if the given text is in English."""
    try:
        return detect(text) == 'en'
    except LangDetectException:
        return False

def split_into_sentences(text):
    """Uses spaCy to split the provided text into sentences, filtering non-English."""
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents if sent.text.strip() != ""]
    # Filter sentences to include only those detected as English
    english_sentences = [sentence for sentence in sentences if is_english(sentence)]
    return english_sentences

def main():
    file_path = 'scraped_articles.csv'
    data = pd.read_csv(file_path)

    # Clean the text
    data['cleaned_text'] = data['Text'].apply(clean_text)

    # Filter for English articles before splitting into sentences
    data['is_english'] = data['cleaned_text'].apply(is_english)
    english_data = data[data['is_english']]

    # Split cleaned text into sentences for manual annotation
    english_data['sentences'] = english_data['cleaned_text'].apply(split_into_sentences)

    sentences_df = english_data.explode('sentences').dropna(subset=['sentences'])
    sentences_df = sentences_df[sentences_df['sentences'].str.strip().astype(bool)]

    annotation_df = sentences_df[['Title', 'sentences']].copy()
    annotation_df.columns = ['Article Title', 'Sentence']
    annotation_df['Fact (Y/N)'] = ""
    
    annotation_df.to_csv('annotation_data_english_only.csv', index=False)
    
    print("Data prepared and exported for annotation. Check annotation_data_english_only.csv.")

if __name__ == "__main__":
    main()
