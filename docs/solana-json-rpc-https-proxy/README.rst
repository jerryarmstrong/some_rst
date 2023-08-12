README.md
=========

Last edited: 2019-07-05 21:43:58

Contents:

.. code-block:: md

    ## Solana JSON RPC HTTPS Proxy

This repository provides an https proxy to the JSON RPC endpoint of a Solana
full node.

## Prerequisites

The machine must have the following:
1. Docker installed
1. TCP ports 80 and 443 available
1. A static IP with an associated FQDN

## Usage:

The following command will create/start a Docker container (restarts on boot) that forwards
https traffic from `my-fullnode-domain.example.com:443` to the standard JSON RPC port of
`my-fullnode-domain.example.com:8899`:
```bash
$ ./start.sh my-fullnode-domain.example.com me@example.com / my-fullnode-domain.example.com
```

For multiple forwards:
```bash
$ ./start.sh api.testnet.solana.com user@example.com \
   /master master.testnet.solana.com \
   / testnet.solana.com
```

Run `./start.sh` with no arguments for more usage information.

## Copyright

This repository is derived from https://github.com/jgoerzen/docker-apache-proxy:
```
Docker scripts, etc. are
Copyright (c) 2018 John Goerzen
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. Neither the name of the University nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHORS AND CONTRIBUTORS ``AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

Additional software copyrights as noted.
```


