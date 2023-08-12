tests/ui/modules/mod_dir_recursive.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-pretty issue #37195

// Testing that the parser for each file tracks its modules
// and paths independently. The load_another_mod module should
// not try to reuse the 'mod_dir_simple' path.

mod mod_dir_simple {
    pub mod load_another_mod;
}

pub fn main() {
    assert_eq!(mod_dir_simple::load_another_mod::test::foo(), 10);
}


