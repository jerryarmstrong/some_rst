tests/ui/parser/trait-item-with-defaultness-pass.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

#[cfg(FALSE)]
trait X {
    default const A: u8;
    default const B: u8 = 0;
    default type D;
    default type C: Ord;
    default fn f1();
    default fn f2() {}
}


