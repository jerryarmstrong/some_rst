tests/ui/modules/mod_dir_path2.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-pretty issue #37195

#[path = "mod_dir_simple"]
mod pancakes {
    #[path = "test.rs"]
    pub mod syrup;
}

pub fn main() {
    assert_eq!(pancakes::syrup::foo(), 10);
}


