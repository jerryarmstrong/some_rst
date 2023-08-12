tests/ui/crate-loading/auxiliary/crateresolve2-1.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-C extra-filename=-1 --emit=metadata
#![crate_name = "crateresolve2"]
#![crate_type = "lib"]

pub fn f() -> isize { 10 }


