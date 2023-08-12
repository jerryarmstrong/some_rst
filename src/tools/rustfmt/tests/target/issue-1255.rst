src/tools/rustfmt/tests/target/issue-1255.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for issue #1255
// Default annotation incorrectly removed on associated types
#![feature(specialization)]

trait Trait {
    type Type;
}
impl<T> Trait for T {
    default type Type = u64; // 'default' should not be removed
}


