tests/rustdoc/test_option_check/test.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --test
// check-test-line-numbers-match

pub mod bar;

/// This is a Foo;
///
/// ```
/// println!("baaaaaar");
/// ```
pub struct Foo;

/// This is a Bar;
///
/// ```
/// println!("fooooo");
/// ```
pub struct Bar;


