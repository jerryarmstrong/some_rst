tests/ui/issues/auxiliary/cgu_test.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // no-prefer-dynamic
// compile-flags: --crate-type=lib

pub fn id<T>(t: T) -> T {
  t
}


