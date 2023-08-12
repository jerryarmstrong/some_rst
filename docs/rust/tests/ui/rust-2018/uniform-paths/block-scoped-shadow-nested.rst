tests/ui/rust-2018/uniform-paths/block-scoped-shadow-nested.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018

mod my {
    pub mod sub {
        pub fn bar() {}
    }
}

mod sub {
    pub fn bar() {}
}

fn foo() {
    use my::sub;
    {
        use sub::bar; //~ ERROR `sub` is ambiguous
    }
}

fn main() {}


