from google.oauth2 import service_account
from googleapiclient.discovery import build
import json

def index_blog_post(url):
    try:
        # Define the path to your service account key
        key_path = "D:\python\PycharmProjects\Saad projects\obbeyan1-1f826ed70d04.json"

        # Define the scopes
        scopes = ['https://www.googleapis.com/auth/indexing']

        # Load the credentials from the service account key file
        credentials = service_account.Credentials.from_service_account_file(key_path, scopes=scopes)

        # Build the service
        service = build('indexing', 'v3', credentials=credentials)

        # Define the content to be indexed
        content = {
            "url": url,
            "type": "URL_UPDATED"
        }

        # Create a request
        request = service.urlNotifications().publish(body=content)

        # Execute the request
        response = request.execute()

        # Print the response
        print("Indexing request successful:")
        print(json.dumps(response, indent=2))

    except Exception as e:
        print("Error occurred while indexing:")
        print(e)

# Define the URL of your blog post
url_to_index = "https://obbeyan1.blogspot.com/2024/03/blog-post_27.html"

# Index the blog post
index_blog_post(url_to_index)
