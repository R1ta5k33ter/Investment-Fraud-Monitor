from functions.pulsedive_request import scan_indicator_and_get_results
from functions.PulseDive_Json_Parser import extract_metadata



def main():

    # Trigger a PulseDive Scan
    result = scan_indicator_and_get_results("futureftrader[.]net")
    print(result)

    # Extract the desired metadata values from the results:
    ip_list, dns_records, registration_date, mx_records = extract_metadata(result)
    print("IP addresses:", ip_list)
    print("DNS records:", dns_records)
    print("Registration date:", registration_date)
    print("MX records:", mx_records)

if __name__ == "__main__":
    main()