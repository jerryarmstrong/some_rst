src/tools/rustfmt/tests/source/issue-2342.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-max_width: 80

struct Foo {
    #[cfg(feature = "serde")] bytes: [[u8; 17]; 5], // Same size as signature::ED25519_PKCS8_V2_LEN
}


