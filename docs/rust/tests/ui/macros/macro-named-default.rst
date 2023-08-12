tests/ui/macros/macro-named-default.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
macro_rules! default {
    ($($x:tt)*) => { $($x)* }
}

default! {
    struct A;
}

impl A {
    default! {
        fn foo(&self) {}
    }
}

fn main() {
    A.foo();
}


