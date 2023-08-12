tests/ui/issues/issue-16922-rpass.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

use std::any::Any;

fn foo(_: &u8) {
}

fn main() {
    let _ = &foo as &dyn Any;
}


