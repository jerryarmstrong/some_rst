solana/src/main/java/com/solana/vendor/bip32/wallet/key/HdPublicKey.java
========================================================================

Last edited: 2023-08-11 20:37:02

Contents:

.. code-block:: java

    package com.solana.vendor.bip32.wallet.key;

/**
 * Defines a key with a given public key
 */
public class HdPublicKey extends HdKey {
    private byte[] publicKey;

    public byte[] getPublicKey() {
        return publicKey;
    }

    public void setPublicKey(byte[] publicKey) {
        this.publicKey = publicKey;
    }
}


