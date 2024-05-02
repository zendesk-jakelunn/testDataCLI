from zendesk_api import ZendeskAPI

def main():
    zendesk = ZendeskAPI('your_api_key', 'your_subdomain')
    zendesk.create_test_tickets(10)
    zendesk.update_test_tickets([123, 456], "Updated comment text")
    zendesk.update_test_users(5)

if __name__ == "__main__":
    main()
