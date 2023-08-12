tests/ui/chalkify/trait-objects.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

use std::fmt::Display;

fn main() {
    let d: &dyn Display = &mut 3;
    d.to_string();
    (&d).to_string();
    let f: &dyn Fn(i32) -> _ = &|x| x + x;
    f(2);
}


