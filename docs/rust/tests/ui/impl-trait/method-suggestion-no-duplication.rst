tests/ui/impl-trait/method-suggestion-no-duplication.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // issue #21405
struct Foo;

fn foo<F>(f: F) where F: FnMut(Foo) {}

fn main() {
    foo(|s| s.is_empty());
    //~^ ERROR no method named `is_empty` found
}


