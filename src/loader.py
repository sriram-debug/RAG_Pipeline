import os
import re
#chunking

def load_chunks(notes_dir: str) -> list[dict]:
    """
    Returns a list of chunks, each chunk is:
    { "source": filename, "chunk_id": int, "text": str }
    """
    chunks = []
    
    for fname in os.listdir(notes_dir):
        if not fname.endswith(".md"):
            continue
        
        fpath = os.path.join(notes_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Split on markdown headers (##, ###) or double newlines
        #this step depends on the format of your data
        raw_chunks = re.split(r'\n(?=#{1,3} )|\n{2,}', content)
        
        for i, chunk in enumerate(raw_chunks):
            chunk = chunk.strip()
            if len(chunk) < 50: 
                continue
            chunks.append({
                "source": fname,
                "chunk_id": i,
                "text": chunk
            })
    
    return chunks