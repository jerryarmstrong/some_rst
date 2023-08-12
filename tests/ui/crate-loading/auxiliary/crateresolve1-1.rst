tests/ui/crate-loading/auxiliary/crateresolve1-1.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C extra-filename=-1
// no-prefer-dynamic
#![crate_name = "crateresolve1"]
#![crate_type = "lib"]

pub fn f() -> isize { 10 }


