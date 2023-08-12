tests/ui/nll/user-annotations/promoted-annotation.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that type annotations are checked in promoted constants correctly.

fn foo<'a>() {
    let x = 0;
    let f = &drop::<&'a i32>;
    f(&x);
    //~^ ERROR `x` does not live long enough
}

fn main() {}


