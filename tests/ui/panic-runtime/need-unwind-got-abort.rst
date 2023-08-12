tests/ui/panic-runtime/need-unwind-got-abort.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-fail
// error-pattern:is incompatible with this crate's strategy of `abort`
// aux-build:needs-unwind.rs
// compile-flags:-C panic=abort
// no-prefer-dynamic

extern crate needs_unwind;

fn main() {}


