tests/ui/parser/impl-item-type-no-body-pass.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

#[cfg(FALSE)]
impl X {
    type Y;
    type Z: Ord;
    type W: Ord where Self: Eq;
    type W where Self: Eq;
}


