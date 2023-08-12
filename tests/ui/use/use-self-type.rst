tests/ui/use/use-self-type.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;

impl S {
    fn f() {}
    fn g() {
        use Self::f; //~ ERROR unresolved import
        pub(in Self::f) struct Z; //~ ERROR failed to resolve: `Self`
    }
}

fn main() {}


