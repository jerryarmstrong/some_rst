tests/ui/compile_error_macro.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    compile_error!("a very descriptive error message"); //~ ERROR: a very descriptive error message
}


