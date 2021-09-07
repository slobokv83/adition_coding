import requests
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('-id', type=int, required=True)

# Parse the argument
args = parser.parse_args()

resp = requests.get(f'http://localhost:5000/user/{args.id}')

print('USER ADVERTS SEEN:', resp.json())