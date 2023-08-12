tests/ui/imports/import-trailing-comma.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use foo::bar::{baz, quux,};

mod foo {
    pub mod bar {
        pub fn baz() { }
        pub fn quux() { }
    }
}

pub fn main() { baz(); quux(); }


