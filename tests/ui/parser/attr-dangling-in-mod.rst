tests/ui/parser/attr-dangling-in-mod.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:expected item

fn main() {
}

#[foo = "bar"]


