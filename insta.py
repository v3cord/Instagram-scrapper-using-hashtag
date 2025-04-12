import time
import random
import csv
from instagrapi import Client

# Define login credentials
USERNAME = "oogy.42"
PASSWORD = "yatrtatrsarvatr"

# Login to Instagram
client = Client()
client.login(USERNAME, PASSWORD)

# Ask for hashtag input
hashtag = input("Enter the hashtag (without #): ").strip()

# Ask for the number of posts to scrape
while True:
    try:
        num_posts = int(input("Enter the number of posts to scrape: "))
        if num_posts > 0:
            break
        else:
            print("⚠️ Please enter a positive number.")
    except ValueError:
        print("⚠️ Invalid input! Please enter a valid number.")

# Fetch posts under the given hashtag
try:
    top_medias = client.hashtag_medias_v1(hashtag, amount=num_posts, tab_key="top")
    print(f"🔍 Found {len(top_medias)} posts under #{hashtag}")
except Exception as e:
    print(f"❌ Error fetching posts: {e}")
    exit()

# Store collected data
user_data = []

# Process each post
for media in top_medias:
    try:
        # Get post details
        username = media.user.username
        user_id = media.user.pk
        likes = media.like_count
        comments = media.comment_count

        # Fetch user details
        user_info = client.user_info_by_username(username)
        followers = getattr(user_info, 'follower_count', 0)
        bio = getattr(user_info, 'biography', 'N/A')

        # Calculate engagement rate
        engagement = ((likes + comments) / followers) * 100 if followers else 0

        # Store user data
        user_data.append([username, followers, likes, comments, engagement, bio])

        print(f"✅ Processed {username} | {followers} followers | {likes} likes | {comments} comments | {engagement:.2f}% engagement.")

        # Mimic human behavior
        time.sleep(random.randint(5, 10))

    except Exception as e:
        print(f"⚠️ Error processing {media.id}: {e}")

# Save data to a CSV file
csv_filename = f"{hashtag}_{num_posts}_posts_data.csv"

if user_data:
    with open(csv_filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Followers", "Likes", "Comments", "Engagement Rate (%)", "Bio"])
        writer.writerows(user_data)
    print(f"\n✅ Data saved to {csv_filename}")
else:
    print("\n⚠️ No posts met the criteria. CSV file was not created.")
