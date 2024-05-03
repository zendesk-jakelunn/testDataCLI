from zendesk_api import ZendeskAPI

def main():
    zendesk = ZendeskAPI('your_email@example.com', 'your_api_token', 'your_subdomain')
    zendesk.create_test_tickets(10)
    zendesk.update_test_tickets([123, 456], "Updated comment text")
    zendesk.update_test_users(5)

if __name__ == "__main__":
    main()
