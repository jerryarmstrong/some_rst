tests/ui/extenv/extenv-too-many-args.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() { env!("one", "two", "three"); } //~ ERROR: env! takes 1 or 2 arguments


