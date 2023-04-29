# DigitalOcean Droplet Restart Script
This Python script uses the DigitalOcean API to restart a droplet on your account.

# Usage
Make sure you have a DigitalOcean API token. You can get one from your DigitalOcean account settings.

Replace 'YOUR_API_TOKEN' with your API token on line 4.

Run the script.

The script will fetch all droplets associated with your account and ask you to choose which droplet you want to restart.

Enter the number of the droplet you want to restart and press enter.

The script will send a POST request to the DigitalOcean API to initiate the reboot process.

The droplet will be restarted.

# Requirements
Python 3
Requests library (can be installed with pip install requests)

# Example

```$ python restart_droplet.py'
The following droplets were found:
1. droplet-1
2. droplet-2
Enter the number of the droplet you want to restart: 2
Rebooting the "droplet-2" droplet...
```

Note: This script only works for DigitalOcean droplets associated with your account.
