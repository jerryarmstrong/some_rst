README.md
=========

Last edited: 2023-06-21 12:57:05

Contents:

.. code-block:: md

    # soulbound

## Developing

### init

First initialize submodules.

```
git submodule update --init --recursive
```

### build

Then build the program (and it's associated dependencies for CPI invocation).

```
cd deps/metaplex-program-library/token-metadata && anchor build and cd ../../../
cd deps/cardinal-staking && anchor build && cd ../../
anchor build
```

### test

Last, run the integration tests against a local network.

```
anchor test
```


