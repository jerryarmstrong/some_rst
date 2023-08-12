tests/ui/panic-runtime/runtime-depend-on-needs-runtime.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // dont-check-compiler-stderr
// aux-build:needs-panic-runtime.rs
// aux-build:depends.rs
// error-pattern:cannot depend on a crate that needs a panic runtime

extern crate depends;

fn main() {}


