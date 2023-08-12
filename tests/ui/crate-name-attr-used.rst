tests/ui/crate-name-attr-used.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags:--crate-name crate_name_attr_used -F unused-attributes

// pretty-expanded FIXME #23616

#![crate_name = "crate_name_attr_used"]

fn main() {}


