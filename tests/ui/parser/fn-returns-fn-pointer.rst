tests/ui/parser/fn-returns-fn-pointer.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// Regression test for #78507.
fn foo() -> Option<fn() -> Option<bool>> {
    Some(|| Some(true))
}
fn main() {}


