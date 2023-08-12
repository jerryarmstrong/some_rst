tests/ui/proc-macro/attributes-on-modules.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

#[identity_attr]
mod m {
    pub struct S;
}

#[identity_attr]
fn f() {
    mod m {}
}

fn main() {
    let s = m::S;
}


