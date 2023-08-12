tests/ui/issues/issue-pr29383.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    enum E {
    A,
    B,
}

fn main() {
    match None {
        None => {}
        Some(E::A(..)) => {}
        //~^ ERROR expected tuple struct or tuple variant, found unit variant `E::A`
        Some(E::B(..)) => {}
        //~^ ERROR expected tuple struct or tuple variant, found unit variant `E::B`
    }
}


