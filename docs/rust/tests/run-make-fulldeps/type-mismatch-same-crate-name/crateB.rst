tests/run-make-fulldeps/type-mismatch-same-crate-name/crateB.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern crate crateA;

pub fn try_foo(x: crateA::Foo){}
pub fn try_bar(x: Box<crateA::Bar>){}


