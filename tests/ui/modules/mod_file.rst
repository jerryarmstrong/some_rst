tests/ui/modules/mod_file.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-pretty issue #37195

// Testing that a plain .rs file can load modules from other source files

mod mod_file_aux;

pub fn main() {
    assert_eq!(mod_file_aux::foo(), 10);
}


