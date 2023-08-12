tests/ui/suggestions/chain-method-call-mutation-in-place.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}
fn foo(mut s: String) -> String {
    s.push_str("asdf") //~ ERROR mismatched types
}


