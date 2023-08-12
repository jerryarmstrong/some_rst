tests/ui/conditional-compilation/cfg-in-crate-1.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: `main` function not found

#![cfg(bar)]


