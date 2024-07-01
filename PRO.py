import requests
from requests_oauthlib import OAuth1

def main():
    # Define your LinkedIn API credentials
    consumer_key = "your linkedin key"
    consumer_secret = "linkedin secret"
    
    # Define the LinkedIn API endpoints
    request_token_url = "https://api.linkedin.com/uas/oauth/requestToken"
    access_token_url = "https://api.linkedin.com/uas/oauth/accessToken"
    authorize_url = "https://api.linkedin.com/uas/oauth/authorize"
    
    # Create an OAuth1 session
    oauth = OAuth1(consumer_key, consumer_secret, signature_method="HMAC-SHA1")
    
    # Fetch the request token
    response = requests.post(url=request_token_url, auth=oauth)
    credentials = response.text.split('&')
    request_token = credentials[0].split('=')[1]
    request_token_secret = credentials[1].split('=')[1]
    
    # Redirect the user to the LinkedIn authorization page
    print("Visit the following URL to authorize the app:")
    auth_url = f"{authorize_url}?oauth_token={request_token}"
    print(auth_url)
    verifier = input("Enter the PIN code from the URL: ")
    
    # Exchange the request token for an access token
    oauth = OAuth1(
        consumer_key,
        consumer_secret,
        request_token,
        request_token_secret,
        verifier=verifier
    )
    response = requests.post(url=access_token_url, auth=oauth)
    credentials = response.text.split('&')
    access_token = credentials[0].split('=')[1]
    access_token_secret = credentials[1].split('=')[1]
    
    # Make an API request using the access token
    api_url = "http://api.linkedin.com/v1/people/~:(id,first-name,last-name,picture-url,headline)"
    oauth = OAuth1(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret,
        signature_method="HMAC-SHA1"
    )
    response = requests.get(url=api_url, auth=oauth)
    
    # Print the API response
    print("Response: " + str(response.status_code) + " " + response.reason)
    print("\n" + response.text)

if __name__ == "_main_":
    main()