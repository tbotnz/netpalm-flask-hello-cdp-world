# netpalm-flask-hello-cdp-world
simple hello world CDP visualisation webapp leveraging netpalm

![netpalm](/netpalm_cdp.gif)

### getting started
- ensure you have a [netpalm](https://github.com/tbotnz/netpalm) container running
- load the ```cdp_service.j2``` service template into your running netpalm instance
- git clone the project ``` git clone https://github.com/tbotnz/netpalm-flask-hello-cdp-world.git && cd netpalm-hello-cdp-world ```
- update the app.py with your ```NETPALM_SERVER_IP``` ```NETPALM_SERVER_PORT``` ```NETPALM_API_KEY```
- install the requirements ```pip3 install -r requirements.txt```
- run the app ```python3 app.py```

### credits
- https://observablehq.com/@d3/mobile-patent-suits
