tests/rustdoc/hidden-line.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    /// The '# ' lines should be removed from the output, but the #[derive] should be
/// retained.
///
/// ```rust
/// # #[derive(PartialEq)] // invisible
/// # struct Foo; // invisible
///
/// #[derive(PartialEq)] // Bar
/// struct Bar(Foo);
///
/// fn test() {
///     let x = Bar(Foo);
///     assert_eq!(x, x); // check that the derivings worked
/// }
/// ```
pub fn foo() {}

// @!hasraw hidden_line/fn.foo.html invisible
// @matches - //pre "#\[derive\(PartialEq\)\] // Bar"


