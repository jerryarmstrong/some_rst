tests/ui/parser/macro/macro-doc-comments-2.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! inner {
    (#![$inner:meta]) => ()
}

inner! {
    /// Outer
} //~^ ERROR no rules expected the token `[`

fn main() { }


