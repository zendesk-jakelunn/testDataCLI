import requests
from faker import Faker

class ZendeskAPI:
    def __init__(self, email, api_token, subdomain):
        self.email = email
        self.api_token = api_token
        self.subdomain = subdomain
        self.base_url = f"https://{subdomain}.zendesk.com/api/v2"
        self.headers = {
            "Content-Type": "application/json"
        }
        self.auth = (f"{email}/token", api_token)
        self.faker = Faker()

    def send_request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, auth=self.auth, json=data, headers=self.headers)
        if not response.ok:
            print(f"Request failed: {response.status_code} {response.text}")
        return response

    def generate_user(self):
        name = self.faker.name()
        first_name, last_name = name.split()[:2]
        domain = self.faker.random.choice(['example.com', 'example.net', 'example.org'])
        email = f"{first_name.lower()}.{last_name.lower()}@{domain}"
        return name, email

    def create_test_tickets(self, num_tickets):
        for _ in range(num_tickets):
            name, email = self.generate_user()
            data = {
                "ticket": {
                    "requester": {
                        "name": name,
                        "email": email
                    },
                    "subject": "Test Ticket",
                    "comment": {
                        "body": self.faker.text()
                    }
                }
            }
            self.send_request('POST', 'tickets.json', data)

    def update_test_tickets(self, ticket_ids, new_text):
        for ticket_id in ticket_ids:
            data = {
                "ticket": {
                    "comment": {
                        "body": new_text
                    }
                }
            }
            self.send_request('PUT', f'tickets/{ticket_id}.json', data)

    def update_test_users(self, num_users):
        users_data = [self.generate_user() for _ in range(num_users)]
        data = {"users": [{"name": name, "email": email} for name, email in users_data]}
        self.send_request('POST', 'users/create_many.json', data)
