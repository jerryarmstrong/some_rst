tests/ui/consts/const-fn-destructuring-arg.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

const fn i((a, b): (u32, u32)) -> u32 {
    a + b
}

fn main() {}


