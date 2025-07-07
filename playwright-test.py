from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        p.firefox.launch()
        p.goto("https://nixos.org")
        print("Title:", p.title())


if __name__ == "__main__":
    main()
