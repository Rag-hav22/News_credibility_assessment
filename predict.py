import joblib
import sys
import os

def load_model():
    # Get the absolute path to the saved_models directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, 'saved_models', 'text_model.pkl')
    vec_path = os.path.join(base_dir, 'saved_models', 'tfidf_vectorizer.pkl')
    
    if not os.path.exists(model_path):
        print("Error: Model files not found. Did you save them in Jupyter first?")
        sys.exit(1)
        
    model = joblib.load(model_path)
    vectorizer = joblib.load(vec_path)
    return model, vectorizer

def predict_news(text):
    model, vectorizer = load_model()
    
    # Process the text and predict
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    prob = model.predict_proba(text_vec)[0]
    
    print("\n" + "="*50)
    print(f"INPUT: {text}")
    print("-" * 50)
    
    # 1 = Real, 0 = Fake (Adjust if your dataset labels differ)
    if prediction == 1:
        print(f"RESULT: ✅ REAL NEWS (Confidence: {prob[1]*100:.1f}%)")
    else:
        print(f"RESULT: 🚨 FAKE NEWS (Confidence: {prob[0]*100:.1f}%)")
    print("="*50 + "\n")

# This allows the script to be run directly from the terminal
if __name__ == "__main__":
    print("AI News Credibility Verifier")
    print("Type a news headline to check (or type 'quit' to exit):")
    
    while True:
        user_input = input("\nHeadline> ")
        if user_input.lower() in ['quit', 'exit', 'q']:
            break
        
        if len(user_input.strip()) > 0:
            predict_news(user_input)