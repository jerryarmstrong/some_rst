tests/ui/chalkify/basic.rs
==========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z trait-solver=chalk

trait Foo {}

struct Bar {}

impl Foo for Bar {}

fn main() -> () {
    let _ = Bar {};
}


