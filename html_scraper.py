import requests
from bs4 import BeautifulSoup

def scrape_html(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if the request failed

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Convert parsed HTML back to a string for saving
        html_content = soup.prettify()

        # Save the HTML content to a file
        with open("scraped_html.html", "w", encoding='utf-8') as file:
            file.write(html_content)

        print(f"HTML content successfully scraped and saved to 'scraped_html.html'.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")

if __name__ == "__main__":
    # Ask the user for the URL to scrape
    url = input("Enter the URL of the webpage to scrape: ")
    scrape_html(url)
