# Email Scraper

This Python script is designed to scrape email addresses from websites, all in a 10-second maximum timeframe. It prompts the user to input the URLs of websites from which they want to extract emails. The script then crawls the provided websites, extracting email addresses from the HTML content and storing them in a CSV file.

## Usage

1. Run the script and input the number of websites from which you want to extract emails.
2. Input the URLs of the websites.
   ![image](https://github.com/MankaranRooprai/email-scraper/assets/13322471/1fbf78eb-7881-4b82-8341-5daa953f3e70)
3. The script will crawl each website, extract email addresses, and store them in a CSV file named "emails.csv" on your desktop.
   ![image](https://github.com/MankaranRooprai/email-scraper/assets/13322471/9959fb21-10b5-47ee-9d0a-c2d68e623eb1)
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
