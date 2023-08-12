tests/ui/extoption_env-too-many-args.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() { option_env!("one", "two"); } //~ ERROR: option_env! takes 1 argument


