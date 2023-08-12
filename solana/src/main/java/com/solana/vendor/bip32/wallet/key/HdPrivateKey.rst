solana/src/main/java/com/solana/vendor/bip32/wallet/key/HdPrivateKey.java
=========================================================================

Last edited: 2023-08-11 20:37:02

Contents:

.. code-block:: java

    package com.solana.vendor.bip32.wallet.key;

/**
 * Defines a key with a given private key
 */
public class HdPrivateKey extends HdKey {
    private byte[] privateKey;

    public byte[] getPrivateKey() {
        return privateKey;
    }

    public void setPrivateKey(byte[] privateKey) {
        this.privateKey = privateKey;
    }
}


