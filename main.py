import requests

url = "https://tiny.pl/"

# You can use any url that raises err 403 (and makes cloudflare appear)
# I am using https://tiny.pl/ for this because its the best looking url for me and it instantly raises the err for no reason.

response = requests.get(url)

if response.status_code == 403:
    if "cloudflare" in response.text:
        cloudflare_response = response.text
        ip = ""
        lines = cloudflare_response.split("\n")
        for line in lines:
            if '<span class="hidden" id="cf-footer-ip">' in line:
                ip = line.strip()
                ip = ip[39:-7]
                break
    print(ip)
else:
    print(response.status_code)
    print("Site did not raise cloudflare.")

input("Press ENTER To Leave.")
