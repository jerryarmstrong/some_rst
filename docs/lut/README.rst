README.md
=========

Last edited: 2022-10-21 22:32:41

Contents:

.. code-block:: md

    ## LUT - A simple CLI for creating and managing Solana Lookup Tables

## Commands

```bash
lut create 
```

Creates a new LUT using the default keypair in the Solana config file.

```bash
lut extend <lut_address> -a <address1> -a <address2> -a <address3>
```

Appends new addresses to the LUT.

```bash
lut deactivate <lut_address>
```

Deactivates the LUT, starting the cooldown period.

```bash
lut close <lut_address>
```

Closes the LUT and returns the rent funds to the owner keypair.

