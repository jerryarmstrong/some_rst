tests/ui/proc-macro/two-crate-types-1.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern: cannot mix `proc-macro` crate type with others

// force-host
// no-prefer-dynamic

#![crate_type = "proc-macro"]
#![crate_type = "rlib"]


