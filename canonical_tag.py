# Sample data: URLs and their corresponding canonical URLs
url_to_canonical = {
    "[1](https://obbeyan1.blogspot.com/?m=1)": "[2](https://obbeyan1.blogspot.com/)",
    "[3](https://obbeyan1.blogspot.com/p/contact-us.html?m=1)": "[4](https://obbeyan1.blogspot.com/p/contact-us.html)",
    "[5](https://obbeyan1.blogspot.com/p/privacy-policy.html?m=1)": "[6](https://obbeyan1.blogspot.com/p/privacy-policy.html)",
    "[7](https://obbeyan1.blogspot.com/p/about-us.html?m=1)": "[8](https://obbeyan1.blogspot.com/p/about-us.html)",
    "[9](https://obbeyan1.blogspot.com/2024/03/Free-text-to-speech-generating-tool-text-to-speech-generator-voice-generator.html?m=1)": "[10](https://obbeyan1.blogspot.com/2024/03/Free-text-to-speech-generating-tool-text-to-speech-generator-voice-generator.html)"
}

def validate_canonical_tags(url_to_canonical):
    for url, canonical_url in url_to_canonical.items():
        if url == canonical_url:
            print(f"Warning: Canonical URL {canonical_url} points to itself for {url}.")
        else:
            print(f"Info: Canonical URL {canonical_url} is correctly set for {url}.")

# Call the function with the provided data
validate_canonical_tags(url_to_canonical)
