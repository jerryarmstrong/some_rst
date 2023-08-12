tests/run-make-fulldeps/rustdoc-error-lines/input.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test for #45868

// random #![feature] to ensure that crate attrs
// do not offset things
/// ```rust
/// #![feature(bool_to_option)]
/// let x: char = 1;
/// ```
pub fn foo() {

}

/// Add some text around the test...
///
/// ```rust
/// #![feature(bool_to_option)]
/// let x: char = 1;
/// ```
///
/// ...to make sure that the line number is still correct.
///
/// Let's also add a second test in the same doc comment.
///
/// ```rust
/// #![feature(bool_to_option)]
/// let x: char = 1;
/// ```
pub fn bar() {}


