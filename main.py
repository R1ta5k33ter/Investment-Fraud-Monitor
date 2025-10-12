from functions.pulsedive_request import scan_indicator_and_get_results
from functions.PulseDive_Json_Parser import extract_ip_and_screenshot



def main():

    # Trigger a PulseDive Scan
    result = scan_indicator_and_get_results("futureftrader[.]net")
    print(result)

    # Extract only the IP and screenshot from results:
    ip, screenshot_url = extract_ip_and_screenshot(result)
    print("IP addresses:", ip)
    print("Screenshot URL:", screenshot_url)




if __name__ == "__main__":
    main()