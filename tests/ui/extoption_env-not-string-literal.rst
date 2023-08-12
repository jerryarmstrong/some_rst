tests/ui/extoption_env-not-string-literal.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() { option_env!(10); } //~ ERROR: argument must be a string literal


