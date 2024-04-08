#!/usr/bin/python3
import os

def generate_robots_txt(domain):
    return f"""User-agent: *
Disallow: /manager/
Disallow: /index.php
Disallow: /email-protection*
Disallow: /?*

Host: https://{domain}/
Sitemap: https://{domain}/sitemap.xml
"""

def main():
    domain = os.environ.get('HTTP_HOST')
    if domain:
        robots_txt_content = generate_robots_txt(domain)
        print("Content-Type: text/plain")
        print()
        print(robots_txt_content)
    else:
        print("Status: 500 Internal Server Error")
        print("Content-Type: text/plain")
        print()
        print("Error: Unable to get the current domain.")

if __name__ == "__main__":
    main()


