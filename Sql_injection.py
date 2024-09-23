from urllib.parse import urlparse, parse_qs

RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def print_banner():
    banner = f"""{GREEN} 
 _   _ _  _   _            _____                       _ 
| \ | | || | | |          / ____|                     | |
|  \| | || |_| |_ _______| (___   __ _ _   _  __ _  __| |
| . ` |__   _| __|_  /_  /\___ \ / _` | | | |/ _` |/ _` |
| |\  |  | | | |_ / / / / ____) | (_| | |_| | (_| | (_| |
|_| \_|  |_|  \__/___/___|_____/ \__, |\__,_|\__,_|\__,_|
                                    | |                  
                                    |_|                  
{RESET}"""
    print(banner)

def get_uri_parameters(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    parsed_params = {key: value[0] for key, value in query_params.items()}
    return parsed_params

def validate_url(url):
    parsed = urlparse(url)
    return bool(parsed.scheme and parsed.netloc)

def main():
    print_banner()
    
    while True:
        url = input(YELLOW + "Enter URL: " + RESET)
        
        if not validate_url(url):
            print(RED + "Invalid URL! Please enter a valid URL." + RESET)
            continue
        
        print(CYAN + "N4tzz-Squad Searching URI Parameters!!" + RESET)
        params = get_uri_parameters(url)
        
        if params:
            print(WHITE + f"\nURI Parameters Found for URL: {url}")
            for key, value in params.items():
                print(f"{key}: {value}")
        else:
            print(WHITE + f"\nNo URI parameters found for URL: {url}")

        repeat = input(YELLOW + "Would you like to search another URL? (yes/no): " + RESET).lower()
        if repeat != 'yes':
            print(WHITE + "Exiting the program." + RESET)
            break

if __name__ == "__main__":
    main()
