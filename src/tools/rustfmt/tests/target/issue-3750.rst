src/tools/rustfmt/tests/target/issue-3750.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // rustfmt-imports_granularity: Crate

pub mod foo {
    pub mod bar {
        pub struct Bar;
    }

    pub fn bar() {}
}

use foo::{bar, bar::Bar};

fn main() {
    bar();
}


