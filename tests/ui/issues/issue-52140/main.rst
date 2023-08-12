tests/ui/issues/issue-52140/main.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:some_crate.rs
// compile-flags:--extern some_crate
// edition:2018

mod foo {
    pub use some_crate;
}

fn main() {
    ::some_crate::hello();
    foo::some_crate::hello();
}


