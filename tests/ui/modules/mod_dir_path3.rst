tests/ui/modules/mod_dir_path3.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-pretty issue #37195

#[path = "mod_dir_simple"]
mod pancakes {
    pub mod test;
}

pub fn main() {
    assert_eq!(pancakes::test::foo(), 10);
}


