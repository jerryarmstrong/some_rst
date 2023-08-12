tests/ui/imports/extern-crate-self/extern-crate-self-pass.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)

extern crate self as foo;

struct S;

mod m {
    fn check() {
        foo::S; // OK
    }
}

fn main() {}


