tests/ui/modules/path-macro.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! foo {
    () => {"bar.rs"};
}

#[path = foo!()] //~ ERROR malformed `path` attribute
mod abc;

fn main() {}


