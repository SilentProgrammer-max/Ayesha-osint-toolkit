# This script finds details about a given IP address (location, ISP, etc.).
import requests

def ip_lookup(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "success":
            print(f"\nIP Address: {data['query']}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"ISP: {data['isp']}")
            print(f"Lat/Lon: {data['lat']}, {data['lon']}")
        else:
            print("Invalid IP or API limit reached.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ip = input("Enter IP address: ")
    ip_lookup(ip)
