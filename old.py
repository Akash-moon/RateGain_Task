from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def get_total_pages(url):
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for some time to let the page load (you might need to adjust this)G
    driver.implicitly_wait(1)

    # Get the page source after waiting
    page_source = driver.page_source

    # Close the browser
    driver.quit()

    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the pagination element
    pagination = soup.find('div', class_='pagination')

    # Extract page numbers
    page_numbers = [int(page.text) for page in pagination.find_all('a', class_='page-numbers') if page.text.isdigit()]

    # Find the maximum page number
    max_page_number = max(page_numbers) if page_numbers else 1

    return max_page_number
def scrape_blog_data(url):
    # Use Selenium to load the page dynamically
    driver = webdriver.Chrome()
    driver.get(url)

    # Wait for some time to let the page load (you might need to adjust this)
    driver.implicitly_wait(5)

    try:
        # Get the page source after waiting
        page_source = driver.page_source

        # Parse the HTML content with Beautiful Soup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Create empty lists to store data
        titles = []
        dates = []
        image_urls = []
        likes_counts = []

        # Find all blog posts
        blog_posts = soup.find_all('article', class_='blog-item')

        for post in blog_posts:
            # Extract blog title
            title = post.find('h6').text.strip()
            titles.append(title)

            # Extract blog date
            date = post.find('div', class_='bd-item').find('span').text.strip()
            dates.append(date)

            # Extract blog image URL
            image_url = post.find('div', class_='img').find('a')['data-bg']
            image_urls.append(image_url)

            # Extract blog likes count
            likes_count = post.find('a', class_='zilla-likes').find('span').text.strip()
            likes_counts.append(likes_count)

        # Create a DataFrame using pandas
        data = {'Title': titles, 'Date': dates, 'Image URL': image_urls, 'Likes Count': likes_counts}
        df = pd.DataFrame(data)

        # Save DataFrame to CSV file, append if file exists
        df.to_csv('blog_data.csv', mode='a', header=not pd.io.common.file_exists('blog_data.csv'), index=False)

    finally:
        # Close the browser window
        driver.quit()

# Example usage
url = "https://rategain.com/blog"
# url = "https://www.commvault.com/blogs"
total_pages = get_total_pages(url)

print(f"The total number of pages on the website is: {total_pages}")

# Example usage in a loop
for page_number in range(1, total_pages):  # Adjust the range based on the number of pages you want to scrape
    url = f"https://rategain.com/blog/page/{page_number}/"
    scrape_blog_data(url)


# it is simple the template i.e without the GUI(tkinter) 
# it is just simple 