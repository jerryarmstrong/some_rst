tests/ui/definition-reachable/private-use.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that private use statements can be used by

// run-pass
// aux-build:private-use-macro.rs

extern crate private_use_macro;

fn main() {
    assert_eq!(private_use_macro::m!(), 57);
}


