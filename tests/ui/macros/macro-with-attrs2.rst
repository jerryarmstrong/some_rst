tests/ui/macros/macro-with-attrs2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#[cfg(foo)]
macro_rules! foo { () => (1) }

#[cfg(not(foo))]
macro_rules! foo { () => (2) }

pub fn main() {
    assert_eq!(foo!(), 2);
}


