tests/ui/parser/impl-item-fn-no-body-pass.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {}

#[cfg(FALSE)]
impl X {
    fn f();
}


