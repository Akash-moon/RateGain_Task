# from selenium import webdriver
# from bs4 import BeautifulSoup
# import pandas as pd
# import argparse
# import tkinter as tk

# def get_total_pages(url):
#     driver = webdriver.Chrome()
#     driver.get(url)

#     # Wait for some time to let the page load (you might need to adjust this)G
#     driver.implicitly_wait(1)

#     # Get the page source after waiting
#     page_source = driver.page_source

#     # Close the browser
#     driver.quit()

#     # Parse the HTML content with Beautiful Soup
#     soup = BeautifulSoup(page_source, 'html.parser')

#     # Find the pagination element
#     pagination = soup.find('div', class_='pagination')

#     # Extract page numbers
#     page_numbers = [int(page.text) for page in pagination.find_all('a', class_='page-numbers') if page.text.isdigit()]

#     # Find the maximum page number
#     max_page_number = max(page_numbers) if page_numbers else 1

#     return max_page_number

# def scrape_blog_data(url,scraped_data):
#     # Use Selenium to load the page dynamically
#     driver = webdriver.Chrome()
#     driver.get(url)

#     # Wait for some time to let the page load (you might need to adjust this)
#     driver.implicitly_wait(5)

#     # Get the page source after waiting
#     page_source = driver.page_source

#     # Close the browser
#     driver.quit()

#     # Parse the HTML content with Beautiful Soup
#     soup = BeautifulSoup(page_source, 'html.parser')

#     # Create empty lists to store data
#     titles = []
#     dates = []
#     image_urls = []
#     likes_counts = []

#     # Find all blog posts
#     blog_posts = soup.find_all('article', class_='blog-item')

#     for post in blog_posts:
#         # Extract blog title
#         title = post.find('h6').text.strip()
#         titles.append(title)

#         # Extract blog date
#         date = post.find('div', class_='bd-item').find('span').text.strip()
#         dates.append(date)

#         # Extract blog image URL
#         image_url = post.find('div', class_='img').find('a')['data-bg']
#         image_urls.append(image_url)

#         # Extract blog likes count
#         likes_count = post.find('a', class_='zilla-likes').find('span').text.strip()
#         likes_counts.append(likes_count)

#     # Create a DataFrame using pandas
#     data = {'Title': titles, 'Date': dates, 'Image URL': image_urls, 'Likes Count': likes_counts}
#     df = pd.DataFrame(data)

#     # Save DataFrame to CSV file, append if file exists
#     # df.to_csv('blog_data.csv', mode='a', header=not pd.io.common.file_exists('blog_data.csv'), index=False)
#     df.to_csv(scraped_data, mode='a', header=not pd.io.common.file_exists(scraped_data), index=False)


# def main():
#     parser = argparse.ArgumentParser(description="Web Scraping Prototype")

#     # Command-line arguments
#     parser.add_argument("url", help="URL of the website to scrape")
#     parser.add_argument("--output", "-o", default="blog_data.csv", help="Output CSV file for storing scraped data")

#     args = parser.parse_args()

#     # Get total pages
#     total_pages = get_total_pages(args.url)
#     print(f"The total number of pages on the website is: {total_pages}")

#     # Scrape data for each page
#     for page_number in range(1, total_pages + 1):
#         url = f"{args.url}/page/{page_number}/"
#         scrape_blog_data(url, args.output)

#     print(f"Scraping completed. Data saved to {args.output}")

# if __name__ == "__main__":
#     main()




# ---------------------------------X-------------------------------------X----------------------------------X---


# ---------------------------------X-------------------------------------X----------------------------------X---



import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import pandas as pd
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pytz
from datetime import datetime

url_entry = None
output_entry = None

def get_total_pages(url):
    options = Options()
    options.add_argument('--headless')  # Run the browser in headless mode


    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)

        # Set an implicit wait of 4 seconds
        # WebDriver will wait for the specified amount of time for it to appear before throwing an exception.
        driver.implicitly_wait(10)
        
        # Get the page source after waiting
        page_source = driver.page_source
        
        # Your existing code for parsing the page goes here
        driver.quit()

    except TimeoutException:
        # Handle the timeout exception
        print("The page took too long to load. Consider increasing the implicit wait time or check the page loading mechanism.")

    # Parse the HTML content with Beautiful Soup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find the pagination element
    pagination = soup.find('div', class_='pagination')

    # Extract page numbers
    page_numbers = [int(page.text) for page in pagination.find_all('a', class_='page-numbers') if page.text.isdigit()]

    # Find the maximum page number
    max_page_number = max(page_numbers) if page_numbers else 1

    return max_page_number

def scrape_blog_data(url,scraped_data,log_file,page_number):

    options = Options()
    options.add_argument('--headless')  # Run the browser in headless mode


    # Use Selenium to load the page dynamically
    driver = webdriver.Chrome(options=options)
    try:
        # Use Selenium to load the page dynamically
        driver.get(url)

        # Wait for some time to let the page load (you might need to adjust this)
        driver.implicitly_wait(10)

        # Get the page source after waiting
        page_source = driver.page_source

        # Your existing code for parsing the page goes here
        driver.quit()

    except TimeoutException:
        # Handle the timeout exception
        print(f"The page took too long to load for page {page_number}. Consider increasing the implicit wait time or check the page loading mechanism.")

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
    df.to_csv(scraped_data, mode='a', header=not pd.io.common.file_exists(scraped_data), index=False)

    # to keep the record 
    current_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    with open(log_file, 'a') as log:
        log.write(f"Scraping of page-{page_number} completed at {current_time}. Data saved to {scraped_data}\n")


def on_scrape_button_click():
    global url_entry, output_entry
    url = url_entry.get("1.0", tk.END).strip()  # Get text content from Text widget
    output_file = output_entry.get("1.0", tk.END).strip()
    log_file = "scraping_log.txt"

    # Edge Cases
    if not (url or output_file):
        messagebox.showerror("Error", "Enter url and file name.")
        return

    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    if not output_file:
        messagebox.showerror("Error", "Give the File Name.")
        return

    # Logic 
    try:
        total_pages = get_total_pages(url)

        if(total_pages == 0):
            return messagebox.showinfo("Info","Nothing to scrap here !")
             
        messagebox.showinfo("Info", f"The total number of pages on the website is: {total_pages}")
        messagebox.showinfo("Info","Start Scraping")

        for page_number in range(1, total_pages + 1):
            page_url = f"{url}/page/{page_number}/"
            scrape_blog_data(page_url, output_file,log_file, page_number)

        messagebox.showinfo("Info", f"Scraping completed. Data saved to {output_file}")
    except Exception as e:
        return messagebox.showerror("Error", f"An error occurred: {str(e)}")

    messagebox.showinfo("Info","Scraping Successful")

# Download image from URL and create PhotoImage
def download_image_from_url(url, blur_radius=2):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    # Apply a slight blur effect
    # img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
    
    return ImageTk.PhotoImage(img)

# Create the main window
def Window():
    global url_entry, output_entry
    root = tk.Tk()
    root.geometry('800x600')
    root.title("RateGain Web Scraping Tool")

    # background- image 
    logo_url = "https://5.imimg.com/data5/SELLER/Default/2023/11/361132850/SU/IV/KK/13745552/rategain-software.jpg"
    logo = download_image_from_url(logo_url, blur_radius=2)

    # Logo Label
    logo_label = tk.Label(root, image=logo)
    logo_label.place(relwidth=1, relheight=1)

    # Information Label
    info_label = ttk.Label(root, text="Welcome to the RateGain Web Scraping Tool!\n      Enter the URL and click 'Scrape Data'.", font=("Helvetica", 21,"bold"), foreground="orange",background="white")
    info_label.place(relx=0.5, rely=0.35, anchor="center")

    # URL entry
    url_label = ttk.Label(root, text="Enter URL:", font=("Helvetica", 12,"bold"), foreground="black",background="white")
    url_label.place(relx=0.36, rely=0.63, anchor="center")

    # Use Font to set the font size
    url_entry_font = tk.font.Font(family="Helvetica", size=12)
    url_entry = tk.Text(root, width=40, height=1, wrap="none", font=url_entry_font, borderwidth=2, relief="solid", spacing1=5)
    url_entry.place(relx=0.52, rely=0.63, anchor="center")

    # Output entry
    output_label = ttk.Label(root, text="Output File:", font=("Helvetica", 12,"bold"), foreground="black",background="white")
    output_label.place(relx=0.36, rely=0.71, anchor="center")

    # Use Font to set the font size
    output_entry_font = tk.font.Font(family="Helvetica", size=12)
    output_entry = tk.Text(root, width=40, height=1, wrap="none", font=output_entry_font, borderwidth=2, relief="solid", spacing1=5)
    output_entry.place(relx=0.52, rely=0.71, anchor="center")
    output_entry.insert(tk.END, "blog_data.csv")

    # Scrape button
    scrape_button = tk.Button(root, text="Scrape Data", command=on_scrape_button_click,width=10,font=("Helvetica", 14,"bold"), borderwidth=2, relief="solid", pady=5,foreground="orange",height=1)
    scrape_button.place(relx=0.444, rely=0.80, anchor="center")

    # give open and close window button 
    close_button = tk.Button(root, text="Stop Scraping", command=root.quit, font=("Helvetica", 14,"bold"), borderwidth=2, relief="solid", pady=5,foreground="orange",width=11,height=1)
    close_button.place(relx=0.594, rely=0.80, anchor="center")

    # Run the Tkinter event loop
    root.mainloop()

Window()

# Run Code
# step-1 : write in ternminal python 'your_file_name.py'
# step-2 : give this url as an input feild ("https://rategain.com/blog")
# step-3 : click on Scrape data and wait a little 

# Deploy Code 
# using Heroku, but its paid
# pyinstaller is to deploy the tkinter or auto-py-to-exe Better GUI version 
# sometimes i dint get the .exe file due to Avast Anti-virus installed , just right click on the Avast And disable 
# Because I had Avast anti-virus installed on my computer it detected my new executable as a malware and it deleted it immediately after compilation and I had to disable for a while like until next restart and then I tested my new app.


