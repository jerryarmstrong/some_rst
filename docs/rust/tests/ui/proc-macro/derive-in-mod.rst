tests/ui/proc-macro/derive-in-mod.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
// aux-build:test-macros.rs

extern crate test_macros;

mod inner {
    use test_macros::Empty;

    #[derive(Empty)]
    struct S;
}

fn main() {}


