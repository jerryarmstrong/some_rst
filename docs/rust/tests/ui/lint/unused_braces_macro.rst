tests/ui/lint/unused_braces_macro.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
pub fn foo<const BAR: bool> () {}

fn main() {
    foo::<{cfg!(feature = "foo")}>();
}


