tests/ui/modules/mod_dir_implicit.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-pretty issue #37195

mod mod_dir_implicit_aux;

pub fn main() {
    assert_eq!(mod_dir_implicit_aux::foo(), 10);
}


