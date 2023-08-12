src/tools/rustfmt/tests/target/unsafe-mod.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // These are supported by rustc syntactically but not semantically.

#[cfg(any())]
unsafe mod m {}

#[cfg(any())]
unsafe extern "C++" {}


