#!/usr/bin/python3
import requests
import csv


# Fetch and print titles of all the posts
def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print status code
    print(f"Status Code: {response.status_code}")

    # If request is successful, then print post titles
    if response.status_code == 200:
        # parse JSON
        posts = response.json()
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch")

# Fetch, convert to Python dictionaries
# and save data into a CSV
def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Prepare data for CSV
        data_to_save = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        # Write to posts.csv
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data_to_save)

        print("Posts saved successfully to posts.csv")
    else:
        print("Failed to  fetch")
