# from https://pypi.org/project/python-chargepoint/
# Jon Staebell 5/31/2025

from python_chargepoint import ChargePoint
from discord_webhook import DiscordWebhook
import os, requests, sys

def call_webhook(webhook_url, output_message): 
    # checks the webhook_url parameter, and if present, uses it to send webhook to Discord
    #
    if webhook_url != "": # if url provided, notify Discord to add alert 
        program_name, _ = os.path.splitext(os.path.basename(sys.argv[0])) # remove path and extension from current program name
        webhook = DiscordWebhook(url=webhook_url, content=f"{program_name}: {output_message}")
        response = webhook.execute()
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print("Error in trying to use Discord Webhook", err)

def get_status(webhook_url,username,password):
    any_charging = False
    try:
        client = ChargePoint(username,password)
        # Get list of home chargers
        chargers = client.get_home_chargers()

        # Check if each charger is plugged in
        for charger_id in chargers:
            status = client.get_home_charger_status(charger_id)

            # Access the 'plugged_in' attribute directly
            plugged_in = status.plugged_in
            print(f"Charger ID {charger_id} plugged in: {plugged_in}")
            if plugged_in: # mark that at least one of the chargers is in use
                any_charging = True
    except:
        print("Error getting chargers")
        call_webhook(webhook_url,"Error getting chargers")

    if not any_charging:
        call_webhook(webhook_url,"Car is not plugged in!")

    return any_charging

def main():
    # get username, password, and webhook_url from environment variables
    username = os.getenv('USERNAME', 'REPLACE_ME')  # secure this value
    password = os.getenv('PASSWORD', 'REPLACE_ME')  # secure this value
    webhook_url = os.getenv('WEBHOOK_URL', '')  # secure this value

# if an argument is supplied, do not invoke the discord webhook
    if len(sys.argv) > 1:
        webhook_url = ""
    get_status(webhook_url,username,password)

if __name__ == "__main__":
    main()

