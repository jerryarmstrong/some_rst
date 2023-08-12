src/tools/clippy/tests/ui/doc_link_with_quotes.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::doc_link_with_quotes)]

fn main() {
    foo()
}

/// Calls ['bar'] uselessly
pub fn foo() {
    bar()
}

/// # Examples
/// This demonstrates issue \#8961
/// ```
/// let _ = vec!['w', 'a', 't'];
/// ```
pub fn bar() {}


