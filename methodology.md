 how four chosen formats will translate into actual Python modules 
### 1. The Text Pipeline (`src/text_engine/`)

- **What it does:** Processes news articles, social media captions, and headlines.
    
- **Tech Stack:**
    
    - NLP Transformer models (e.g., RoBERTa, DeBERTa) for stance detection (does the headline match the body?).
        
    - Named Entity Recognition (NER) to extract names, dates, and locations.
        
    - Fact-check API integration (e.g., Google Fact Check Tools API) to search extracted claims against known databases.
        

### 2. The Web & Metadata Pipeline (`src/meta_engine/`)

- **What it does:** Acts as the first line of defense before heavy AI models even run.
    
- **Tech Stack:**
    
    - WHOIS / Python `whois` library to check domain age (newly created domains posting news are highly suspicious).
        
    - URL reputation checkers (e.g., VirusTotal API or custom blocklists).
        
    - Web scraping (BeautifulSoup) to check if an article has an author bio or just a generic "Admin" tag.
        

### 3. The Image Pipeline (`src/image_engine/`)

- **What it does:** Analyzes standalone news photos, screenshots, and memes.
    
- **Tech Stack:**
    
    - **Visual Forensics:** Error Level Analysis (ELA) using OpenCV to detect hidden Photoshop splices.
        
    - **Context Verification:** Reverse image search automation to see if a "current" photo is actually from a 10-year-old event.
        
    - **Synthetic Detection:** A Vision Transformer (ViT) or CNN trained to spot AI-generated artifacts (Midjourney/DALL-E).
        

### 4. The Video Pipeline (`src/video_engine/`)

- **What it does:** Analyzes TikToks, YouTube shorts, and news broadcasts.
    
- **Tech Stack:**
    
    - **Keyframe Extraction:** Using `FFmpeg` or OpenCV to chop the video into 1 frame per second.
        
    - **Routing:** Once the video is chopped into frames, you simply pass those frames through your **Image Pipeline**.
        
    - **OCR:** Extracting any text overlay (like news tickers at the bottom of the screen) using Tesseract OCR, then passing that text to your **Text Pipeline**.