tests/run-make-fulldeps/allow-warnings-cmdline-stability/foo.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(unstable_test_feature)]

extern crate bar;

pub fn main() { bar::baz() }


