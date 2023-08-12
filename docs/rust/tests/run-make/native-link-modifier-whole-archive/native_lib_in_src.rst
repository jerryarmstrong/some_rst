tests/run-make/native-link-modifier-whole-archive/native_lib_in_src.rs
======================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::io::Write;

#[link(name = "c_static_lib_with_constructor",
       kind = "static",
       modifiers = "-bundle,+whole-archive")]
extern {}

pub fn hello() {
    print!("native_lib_in_src.");
    std::io::stdout().flush().unwrap();
}


