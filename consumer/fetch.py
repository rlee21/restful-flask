import requests


def fetch(endpoint):
    response = requests.get(endpoint)
    return response.json()

if __name__ == '__main__':
    endpoint = 'http://product-service'
    # endpoint = 'http://localhost:5000'
    books = fetch(endpoint)
    for book in books['products']:
        print(book)
