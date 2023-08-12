tests/ui/impl-trait/no-trait.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() -> impl 'static {} //~ ERROR at least one trait must be specified

fn main() {}


