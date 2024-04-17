import requests

def get_random_joke():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "text/plain"})
    joke = response.text
    return joke

def main():
    random_joke = get_random_joke()
    print("Random Joke:")
    print(random_joke)

if __name__ == "__main__":
    main()
