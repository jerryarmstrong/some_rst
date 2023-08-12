client/dexterity/scripts/keypair_to_b58.py
==========================================

Last edited: 2022-07-25 20:14:14

Contents:

.. code-block:: py

    import argparse
import json
from base58 import b58encode as b58e
from solana.keypair import Keypair

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("f")
    args = ap.parse_args()

    with open(args.f, "r") as f:
        kp = json.load(f)
    print(b58e(bytes(kp)).decode('ascii'))
    print(Keypair(kp[:32]).public_key)

if __name__ == '__name__':
    main()


