docker/README.md
================

Last edited: 2020-05-01 16:51:26

Contents:

.. code-block:: md

    # Docker

This directory contains [Docker](https://www.docker.com/) configuration and scripts for building images of the validator node, faucet server and client.

## Building Docker images

1. [Download](https://docs.docker.com/install/) and install Docker.
2. From the top level directory, run `docker/validator/build.sh`
3. From the top level directory, run `docker/mint/build.sh`
4. To test the validator image locally, run `docker/validator/run.sh`
5. To test the faucet server image locally, run `docker/mint/run.sh`
6. Run the client as follows:
   `cargo run -p client --bin client -- -a localhost -p 8000 -f localhost:8080 -s terraform/validator-sets/dev/consensus_peers.config.toml`


