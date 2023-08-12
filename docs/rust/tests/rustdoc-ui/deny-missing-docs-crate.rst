tests/rustdoc-ui/deny-missing-docs-crate.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(missing_docs)] //~ ERROR

pub struct Foo; //~ ERROR


