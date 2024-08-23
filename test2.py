import requests 

def check_directory_listing(url):
    try:
        response = requests.get(url)
        if response.status_code == 200 and "<title>Index of /" in response.text:
            return True
        else:
            return False
    except requests.RequestsException:
        return False
if __name__ == "_main_":
        target_url = input("Enter the target URL (e.g, http://example.com/): ")
        if check_directory_listing(target_url):
            print(f"Directory listing is enabled on {target_url}")
        else:
            print(f"Directory listing is not enabled on {target_url}")