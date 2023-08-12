tests/run-make/native-link-modifier-whole-archive/indirectly_linked.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate rlib_with_cmdline_native_lib;

fn main() {
    rlib_with_cmdline_native_lib::hello();
}


