Zendesk Test Tools CLI - Updated 6/5/24

Overview
The Zendesk Test Tools CLI is a Python-based command line tool designed to interact with the Zendesk API. It simplifies the process of:
- Generating test tickets
- Updating test tickets
- Generating test users

Prerequisites
Before proceeding, ensure that you meet the following requirements:
- Python version 3.6 or higher installed on your machine
- Access to a Zendesk account with permissions to obtain an API token

Setup Instructions

1. Clone the Repository
To get started, clone this repository to your local machine and navigate into the directory:
git clone https://github.com/zendesk-jakelunn/testDataCLI.git
cd zendesk_scripts

2. Install Dependencies
Create a virtual environment and activate it. Then, install the necessary Python packages:
python -m venv venv
source venv/bin/activate  # Use 'venv\Scripts\activate' on Windows
pip install -r requirements.txt

3. Update Configuration
Modify the src/zendesk_api.py file to include your Zendesk credentials. Replace the placeholders with your actual data:
zendesk = ZendeskAPI('your_email@example.com', 'your_api_token', 'your_subdomain')
- your_email@example.com: Your Zendesk account email
- your_api_token: Your Zendesk API token
- your_subdomain: Your Zendesk subdomain

Running the Script

Execute the script from the project directory to start interacting with the Zendesk API:
python src/main.py

Usage Examples
Interactive prompts will guide you through the different operations available:
- Create Tickets: Respond 'yes' to create a specified number of test tickets.
- Update Tickets: Respond 'yes' to update specific tickets with new text.
- Create Users: Respond 'yes' to generate a specified number of test users.

Example Interaction
Do you want to create tickets? (yes/no): yes
How many tickets would you like to create?: 10
Do you want to update tickets? (yes/no): yes
Enter ticket IDs to update, separated by commas (e.g., 123,456): 123,456
Enter new text for updating tickets: Update text here
Do you want to create users? (yes/no): no
