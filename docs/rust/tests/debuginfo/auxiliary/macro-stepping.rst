tests/debuginfo/auxiliary/macro-stepping.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-g

#![crate_type = "rlib"]

#[macro_export]
macro_rules! new_scope {
    () => {
        let x = 1;
    }
}


