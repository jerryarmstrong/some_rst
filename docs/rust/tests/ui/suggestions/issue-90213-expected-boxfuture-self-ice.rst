tests/ui/suggestions/issue-90213-expected-boxfuture-self-ice.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Checks that we do not ICE when comparing `Self` to `Pin`
// edition:2021

struct S;

impl S {
    fn foo(_: Box<Option<S>>) {}
    fn bar() {
        Self::foo(None) //~ ERROR mismatched types
    }
}

fn main() {}


