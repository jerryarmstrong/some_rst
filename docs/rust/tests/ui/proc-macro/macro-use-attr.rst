tests/ui/proc-macro/macro-use-attr.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// aux-build:test-macros.rs

#[macro_use]
extern crate test_macros;

#[identity_attr]
struct Foo;

fn main() {
    let _ = Foo;
}


