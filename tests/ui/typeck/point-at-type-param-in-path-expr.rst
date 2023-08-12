tests/ui/typeck/point-at-type-param-in-path-expr.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T: std::fmt::Display>() {}

fn main() {
    let x = foo::<()>;
    //~^ ERROR `()` doesn't implement `std::fmt::Display`
}


