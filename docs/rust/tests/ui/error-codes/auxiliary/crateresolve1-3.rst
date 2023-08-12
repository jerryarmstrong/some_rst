tests/ui/error-codes/auxiliary/crateresolve1-3.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C extra-filename=-3
// no-prefer-dynamic
#![crate_name = "crateresolve1"]
#![crate_type = "lib"]

pub fn f() -> isize { 30 }


