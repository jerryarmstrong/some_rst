src/tools/clippy/tests/ui-cargo/module_style/pass_no_mod/src/main.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::mod_module_files)]

mod good;

fn main() {
    let _ = good::Thing;
}


