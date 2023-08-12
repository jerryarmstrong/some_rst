tests/ui/macros/macro-with-attrs1.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// compile-flags: --cfg foo


#[cfg(foo)]
macro_rules! foo { () => (1) }

#[cfg(not(foo))]
macro_rules! foo { () => (2) }

pub fn main() {
    assert_eq!(foo!(), 1);
}


