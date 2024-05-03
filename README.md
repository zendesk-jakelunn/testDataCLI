
```markdown
# Zendesk Test Tools CLI 

## Overview
This project contains a Python script for interacting with the Zendesk API. It enables the creation and updating of tickets and users in Zendesk based on user input. The script uses token-based authentication to securely access the Zendesk API.

## Prerequisites
Before you begin, ensure you have the following:
- Python 3.6 or later installed on your machine.
- A Zendesk account and access to obtain an API token.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using Git:
```
git clone https://github.com/your-username/zendesk_scripts.git
cd zendesk_scripts
```

### 2. Install Dependencies
Set up a virtual environment and install the required Python packages:
```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Update Configuration
Navigate to the `src/zendesk_api.py` file and update the placeholders in the `ZendeskAPI` class constructor with your Zendesk credentials:
- `your_email@example.com`: Replace this with your Zendesk account email.
- `your_api_token`: Replace this with your Zendesk API token.
- `your_subdomain`: Replace this with your Zendesk subdomain.

```python
zendesk = ZendeskAPI('your_email@example.com', 'your_api_token', 'your_subdomain')
```

## Running the Script

To run the script, navigate to the project directory and execute the `main.py` script:
```
python src/main.py
```

### Usage Examples

- **Create Tickets**: When prompted, choose 'yes' to create tickets and specify the number of tickets to create.
- **Update Tickets**: Choose 'yes' to update tickets, provide the ticket IDs and the new text for the updates.
- **Create Users**: Opt 'yes' to create users and specify how many users you want to create.

Here is what an interaction might look like:
```
Do you want to create tickets? (yes/no): yes
How many tickets would you like to create?: 10
Do you want to update tickets? (yes/no): yes
Enter ticket IDs to update, separated by commas (e.g., 123,456): 123,456
Enter new text for updating tickets: Update text here
Do you want to create users? (yes/no): no
```
```
