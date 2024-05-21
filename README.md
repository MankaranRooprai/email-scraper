# Email Scraper

This Python script is designed to scrape email addresses from websites. It prompts the user to input the URLs of websites from which they want to extract emails. The script then crawls the provided websites, extracting email addresses from the HTML content and storing them in a CSV file.

## Usage

1. Run the script and input the number of websites from which you want to extract emails.
2. Input the URLs of the websites.
3. The script will crawl each website, extract email addresses, and store them in a CSV file named "emails.csv" on your desktop.
4. If a website takes too long to crawl (more than 10 seconds), the script moves on to the next website.

## Dependencies

- Python 3.x
- BeautifulSoup4
- Requests
- Pandas

## Note

Ensure that you have proper permissions to write files on your desktop. If the script encounters any issues with writing the CSV file, it will prompt you to close the file.

## Contributors

- Mankaran Rooprai
