tests/ui/parser/import-from-rename.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // error-pattern:expected

use foo::{bar} as baz;

mod foo {
    pub fn bar() {}
}

fn main() {
}


