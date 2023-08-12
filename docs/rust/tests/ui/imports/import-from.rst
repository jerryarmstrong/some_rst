tests/ui/imports/import-from.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use spam::{ham, eggs};

mod spam {
    pub fn ham() { }
    pub fn eggs() { }
}

pub fn main() { ham(); eggs(); }


