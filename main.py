import requests

#Define API key and droplet name
api_token = 'YOUR_API_TOKEN'
droplet_name = ''

#Send GET request to DigitalOcean API and fetch all droplets
header = {'Authorization': 'Bearer %s' % api_token}
url = 'https://api.digitalocean.com/v2/droplets'
response = requests.get(url, headers=header).json()

#Print all droplets on the screen and ask the user to choose a droplet
droplets = response['droplets']
if len(droplets) > 0:
    print('The following droplets were found:')
    for i, droplet in enumerate(droplets):
        print(str(i+1) + '. ' + droplet['name'])
    droplet_choice = input('Enter the number of the droplet you want to restart: ')
    if droplet_choice.isdigit() and int(droplet_choice) <= len(droplets):
        droplet_id = droplets[int(droplet_choice)-1]['id']
        droplet_name = droplets[int(droplet_choice)-1]['name']
    else:
        print('Invalid droplet number')
else:
    print('No droplets found')

#Get the selected droplet's ID and send a POST request for the reboot process
if droplet_name != '':
    url = 'https://api.digitalocean.com/v2/droplets/%s/actions' % droplet_id
payload = {'type': 'reboot'}
response = requests.post(url, headers=header, json=payload)
print('Rebooting the "%s" droplet...' % droplet_name)