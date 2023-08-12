tests/ui/macros/macro-deep_expansion.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

macro_rules! foo2 {
    () => {
        "foo"
    }
}

macro_rules! foo {
    () => {
        foo2!()
    }
}

fn main() {
    assert_eq!(concat!(foo!(), "bar"), "foobar")
}


