tests/ui/codemap_tests/bad-format-args.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    format!(); //~ ERROR requires at least a format string argument
    format!("" 1); //~ ERROR expected `,`, found `1`
    format!("", 1 1); //~ ERROR expected one of
}


