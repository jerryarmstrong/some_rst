tests/ui/shadowed/shadowed-trait-methods.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that methods from shadowed traits cannot be used

mod foo {
    pub trait T { fn f(&self) {} }
    impl T for () {}
}

mod bar { pub use foo::T; }

fn main() {
    pub use bar::*;
    struct T;
    ().f() //~ ERROR no method
}


