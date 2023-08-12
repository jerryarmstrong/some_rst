tests/run-make/native-link-modifier-whole-archive/rlib_with_cmdline_native_lib.rs
=================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::io::Write;

pub fn hello() {
    print!("indirectly_linked.");
    std::io::stdout().flush().unwrap();
}


