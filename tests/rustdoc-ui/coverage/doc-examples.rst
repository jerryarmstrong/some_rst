tests/rustdoc-ui/coverage/doc-examples.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags:-Z unstable-options --show-coverage
// check-pass

//! This test ensure that only rust code examples are counted.

/// Doc
///
/// ```
/// let x = 2;
/// ```
pub struct Foo;

/// Doc
///
/// ```text
/// yolo
/// ```
pub trait Bar {}

/// Doc
///
/// ```ignore (just for the sake of this test)
/// let x = 2;
/// ```
pub fn foo<T: Bar, D: ::std::fmt::Debug>(a: Foo, b: u32, c: T, d: D) -> u32 {
    0
}


