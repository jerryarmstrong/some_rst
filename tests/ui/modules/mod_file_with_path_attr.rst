tests/ui/modules/mod_file_with_path_attr.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-pretty issue #37195

// Testing that a plain .rs file can load modules from other source files

#[path = "mod_file_aux.rs"]
mod m;

pub fn main() {
    assert_eq!(m::foo(), 10);
}


