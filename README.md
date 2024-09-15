# home-server
Rapsberry Pi configurations for self-hosted apps.

## Preconfiguration

1. Establish a SSH connection with your raspberry pi
2. Update your raspberry pi packages: `sudo apt-get update; sudo apt-get upgrade -y`
3. Install git: `sudo apt-get install git -y`
4. Install docker: `mkdir tmp; curl -fsSL https://test.docker.com -o tmp/get-docker.sh; sudo sh tmp/get-docker.sh; rm -r tmp`
5. Add your user to docker group: `sudo usermod -aG docker <user>`
6. Login: `su - leonidas`
7. Set a static IP: `sudo nmcli con mod "{interface}" ipv4.addresses "{static_ip}/24" ipv4.gateway "{router_ip}" ipv4.dns "{router_ip}" ipv4.method manual`, where:
    * {interface} -> Interface to configure
    * {static_ip} -> An available IP address to assign
    * {router_ip} -> Router IP address
8. Restart raspberry pi network manager: `sudo systemctl restart NetworkManager`

After these steps, you are good to go!


## How to use

Tbd

### Argon Neo 5 m.2 case installation links
- curl https://download.argon40.com/argon-eeprom.sh | bash
- curl https://download.argon40.com/argonneo5.sh | bash

### Mount drive
```bash
sudo fdisk -l # To list all detected devices
sudo mkdir /mnt/data # create data location
sudo ntfslabel /dev/nvme0n1 MEDIA # label disk
sudo mount /dev/nvme0n1 /mnt/data # mount labelled disk
```

### Home Assistant configuration

1. In integrations section, add MQTT Broker.
2. Add mosquitto as broker, leave the rest as default.


## After installation

Map each service to the static IP if you didn't specified your raspberry pi as your LAN DNS.


Future work
* Better documentation for further use
* Robust python scripts
* Add monitoring
* Use ansible to automate these configurations