tests/ui/panic-runtime/unwind-tables-target-required.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that the compiler errors if the user tries to turn off unwind tables
// when they are required.
//
// only-x86_64-windows-msvc
// compile-flags: -C force-unwind-tables=no
//
// error-pattern: target requires unwind tables, they cannot be disabled with `-C force-unwind-tables=no`.

pub fn main() {
}


