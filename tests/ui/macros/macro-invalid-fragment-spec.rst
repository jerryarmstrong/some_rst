tests/ui/macros/macro-invalid-fragment-spec.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo(
    ($x:foo) => ()
    //~^ ERROR invalid fragment specifier
);

fn main() {
    foo!(foo);
}


