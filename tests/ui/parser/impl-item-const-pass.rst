tests/ui/parser/impl-item-const-pass.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

#[cfg(FALSE)]
impl X {
    const Y: u8;
}


