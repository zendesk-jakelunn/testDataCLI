from zendesk_api import ZendeskAPI

def main():
    zendesk = ZendeskAPI('your_email@example.com', 'your_api_token', 'your_subdomain')

    # Ask user what operations they want to perform
    create_tickets = input("Do you want to create tickets? (yes/no): ").lower() == 'yes'
    update_tickets = input("Do you want to update tickets? (yes/no): ").lower() == 'yes'
    create_users = input("Do you want to create users? (yes/no): ").lower() == 'yes'

    if create_tickets:
        num_tickets = int(input("How many tickets would you like to create?: "))
        zendesk.create_test_tickets(num_tickets)
    
    if update_tickets:
        ticket_ids = input("Enter ticket IDs to update, separated by commas (e.g., 123,456): ")
        ticket_ids = [int(id.strip()) for id in ticket_ids.split(',')]
        new_text = input("Enter new text for updating tickets: ")
        zendesk.update_test_tickets(ticket_ids, new_text)

        # TODO: Add ability to specify the requester or author of the update to simulate end-user updates.

    if create_users:
        num_users = int(input("How many users would you like to create?: "))
        zendesk.update_test_users(num_users)

if __name__ == "__main__":
    main()
