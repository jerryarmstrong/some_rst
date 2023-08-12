tests/ui/inner-attrs-on-impl.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

struct Foo;

impl Foo {
    #![cfg(cfg_that_surely_doesnt_exist)]

    fn method(&self) -> bool { false }
}

impl Foo {
    #![cfg(not(cfg_that_surely_doesnt_exist))]

    // check that we don't eat attributes too eagerly.
    #[cfg(cfg_that_surely_doesnt_exist)]
    fn method(&self) -> bool { false }

    fn method(&self) -> bool { true }
}


pub fn main() {
    assert!(Foo.method());
}


