tests/ui/parser/import-glob-rename.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:expected

use foo::* as baz;

mod foo {
    pub fn bar() {}
}

fn main() {
}


