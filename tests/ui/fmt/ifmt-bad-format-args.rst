tests/ui/fmt/ifmt-bad-format-args.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    format_args!(); //~ ERROR: requires at least a format string argument
    format_args!(|| {}); //~ ERROR: must be a string literal
}


