def extract_ip_and_screenshot(api_response):
    """
    Extract IP addresses from 'dns' -> 'a' and screenshot URL from API response.
    
    Parameters:
        api_response (dict): The full JSON response parsed as Python dict.

    Returns:
        tuple: (ip_list, screenshot_url)
            ip_list: list of IP addresses (strings), or empty list if none
            screenshot_url: string URL or None if missing
    """
    data = api_response.get('data', {})
    
    # Extract IP addresses (list) or empty list if missing
    ip_list = data.get('properties', {}).get('dns', {}).get('a', [])
    
    # Extract screenshot URL if present (assuming at top level of 'data')
    screenshot_url = data.get('screenshot')
    
    return ip_list, screenshot_url


# Example: Assuming 'response' holds your JSON as a dict
# ip, screenshot_url = extract_ip_and_screenshot(response)
# print("IP addresses:", ip)
# print("Screenshot URL:", screenshot_url)
