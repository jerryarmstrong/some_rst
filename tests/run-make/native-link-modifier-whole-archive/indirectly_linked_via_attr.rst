tests/run-make/native-link-modifier-whole-archive/indirectly_linked_via_attr.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate native_lib_in_src;

fn main() {
    native_lib_in_src::hello();
}


