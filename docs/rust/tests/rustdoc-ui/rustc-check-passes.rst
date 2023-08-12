tests/rustdoc-ui/rustc-check-passes.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustdoc_internals)]
#![feature(rustdoc_internals)] //~ ERROR

pub fn foo() {}


