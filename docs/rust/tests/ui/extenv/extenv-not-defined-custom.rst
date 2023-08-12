tests/ui/extenv/extenv-not-defined-custom.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() { env!("__HOPEFULLY_NOT_DEFINED__", "my error message"); } //~ ERROR: my error message


