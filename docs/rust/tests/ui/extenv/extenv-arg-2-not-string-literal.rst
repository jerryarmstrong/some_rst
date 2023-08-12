tests/ui/extenv/extenv-arg-2-not-string-literal.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() { env!("one", 10); } //~ ERROR: expected string literal


