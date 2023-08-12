tests/ui/imports/issue-8640.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[allow(unused_imports)]

mod foo {
    use baz::bar;
    mod bar {}
    //~^ ERROR the name `bar` is defined multiple times
}
mod baz { pub mod bar {} }

fn main() {}


