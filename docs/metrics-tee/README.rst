README.md
=========

Last edited: 2020-09-25 20:09:31

Contents:

.. code-block:: md

    # metrics-tee

Metrics-tee is a simple node.js http service that accepts http requests and forwards them to multiple other endpoints. It was built to send [Solana](https://solana.com/) node metrics to multiple influxdb instances.

## Prerequisites

Make sure you have installed the following prerequisites on your machine:
* [node.js](https://nodejs.org/en/) and npm

```bash
sudo apt install -y nodejs npm
```
* [pm2](https://pm2.io/) process manager for Node.js apps (optional)

```bash
npm install pm2 -g
```

## Installation

```bash
git clone https://github.com/coverlet/metrics-tee.git
cd metrics-tee
npm i
```
Rename `config.sample.json` to `config.json` and add all the endpoints that you want the metrics to be forwarded to:
```text
{
    "port": 3311,
    "endpoints": [
        "https://metrics.solana.com:8086/write?db=netdb&u=user&p=pass&precision=ms",
        "http://yourinfluxdcinstance.com:8096/write?db=db&u=user&p=pass&precision=ms",
        ...
    ]
}
```

## Running

Point solana metrics config env variable to the metrics-tee instance:
```bash
Environment="SOLANA_METRICS_CONFIG=host=http://127.0.0.1:3311,db=a,u=a,p=a"
```
Note that `db=a,u=a,p=a` are not used (you already configured the influxdb config for each endpoint in `config.js`), but if they are not present the node will not export the metrics.

### Run with PM2
Build and start the app with pm2:
```bash
npm run pm2
```
Make sure the process starts on system reboot:
 ```bash
pm2 startup
pm2 save
```

### Run with systemd
Alternatively, you can use systemd service manager to handle app execution. In your `.service` file, use this for ExecStart:
```bash
ExecStart=/usr/bin/node /path/to/metrics-tee/build/index.js
```


