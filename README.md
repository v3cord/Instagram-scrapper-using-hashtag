# Instagram Hashtag Scraper

This Python script uses the [instagrapi](https://github.com/adw0rd/instagrapi) library to scrape public post data from Instagram based on a given hashtag. It collects information such as usernames, follower count, likes, comments, engagement rate, and bio, and saves it to a CSV file.

## 🚀 Features

- Login to Instagram using credentials
- Input custom hashtag and number of posts
- Scrapes top posts under the hashtag
- Calculates engagement rate for each user
- Outputs results to a structured CSV file
- Mimics human behavior with random delays

## 🛠️ Requirements

- Python 3.7+
- instagrapi

Install dependencies using:

```bash
pip install -r requirements.txt
📦 Output

CSV file named as: <hashtag>_<number>_posts_data.csv
Example: coding_100_posts_data.csv
⚠️ Note

    Instagram may temporarily restrict actions if scraping is done too aggressively.

    Use a secondary or test account for login to avoid affecting your main account.

    This script only works for public posts and profiles.
📝 Usage

python insta.py

You will be prompted to enter:

    Instagram hashtag (without #)

    Number of posts to scrape
