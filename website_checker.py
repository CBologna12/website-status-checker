import requests
import csv

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        return "Online" if response.status_code == 200 else f"Error {response.status_code}"
    except requests.RequestException:
        return "Offline"

def main():
    urls = [
        "https://google.com",
        "https://github.com",
        "https://thiswebsitedoesnotexist123.com"
    ]

    results = []
    for url in urls:
        status = check_website(url)
        print(f"{url} is {status}")
        results.append({"URL": url, "Status": status})

    with open("status_report.csv", "w", newline="") as csvfile:
        fieldnames = ["URL", "Status"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

if __name__ == "__main__":
    main()

