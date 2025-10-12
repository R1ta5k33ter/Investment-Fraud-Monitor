import os
import time
import requests
from dotenv import load_dotenv

# own functions:
from functions.refang_IOCs import refang_domain



load_dotenv()
API_KEY = os.getenv("PulseDive_API_Key")

def scan_indicator_and_get_results(indicator):
    # refang IOC for API submission:
    indicator = refang_domain(indicator)
    # Step 1: Add indicator to the queue (active probe)
    url = "https://pulsedive.com/api/analyze.php"
    payload = {
        "value": indicator,
        "probe": "0",          # 1 = active scan, 0 = passive
        "pretty": "1",         # Pretty JSON formatting
        "key": API_KEY
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    }
    resp = requests.post(url, data=payload, headers=headers)
    resp.raise_for_status()
    scan_result = resp.json()
    qid = scan_result.get("qid")
    if not qid:
        raise Exception(f"No QID returned: {scan_result}")


    # For troupbleshooting:
    print("qid: ", qid)


    # Step 2: Poll for results using QID
    result_payload = {
        "qid": qid,
        "pretty": "1",
        "key": API_KEY
    }
    for attempt in range(10):  # Try up to ~10*20 seconds
        print(f"Polling attempt {attempt+1}/{10} ...") # informing the user of progress
        result_resp = requests.get(url, params=result_payload)
        print(requests.get(url, params=result_payload)) # for troubleshooting
        result_resp.raise_for_status()
        result_data = result_resp.json()
        if result_data.get("success"):
            return result_data
        time.sleep(20)
    raise TimeoutError("Scan results not ready after 200 seconds.")

# Example usage:
# result = scan_indicator_and_get_results("example.com")
# print(result)