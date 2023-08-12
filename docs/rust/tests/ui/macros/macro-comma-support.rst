tests/ui/macros/macro-comma-support.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This is a companion to the similarly-named test in run-pass.
//
// It tests macros that unavoidably produce compile errors.

fn compile_error() {
    compile_error!("lel"); //~ ERROR lel
    compile_error!("lel",); //~ ERROR lel
}

fn main() {}


