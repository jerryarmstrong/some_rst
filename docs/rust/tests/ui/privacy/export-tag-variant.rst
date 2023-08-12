tests/ui/privacy/export-tag-variant.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub fn x() { }

    enum Y { Y1 }
}

fn main() { let z = foo::Y::Y1; } //~ ERROR: enum `Y` is private


