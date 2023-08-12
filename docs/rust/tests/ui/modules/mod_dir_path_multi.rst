tests/ui/modules/mod_dir_path_multi.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-pretty issue #37195

#[path = "mod_dir_simple"]
mod biscuits {
    pub mod test;
}

#[path = "mod_dir_simple"]
mod gravy {
    pub mod test;
}

pub fn main() {
    assert_eq!(biscuits::test::foo(), 10);
    assert_eq!(gravy::test::foo(), 10);
}


