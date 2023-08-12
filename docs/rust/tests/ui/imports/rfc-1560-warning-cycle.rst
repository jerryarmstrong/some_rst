tests/ui/imports/rfc-1560-warning-cycle.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    pub struct Foo;

mod bar {
    struct Foo;

    mod baz {
        use *;
        use bar::*;
        fn f(_: Foo) {} //~ ERROR `Foo` is ambiguous
    }
}

fn main() {}


