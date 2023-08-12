tests/ui/macros/macro-tt-matchers.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass (FIXME(62277): could be check-pass?)
#![allow(dead_code)]

macro_rules! foo {
    ($x:tt) => (type Alias = $x<i32>;)
}

foo!(Box);


fn main() {}


