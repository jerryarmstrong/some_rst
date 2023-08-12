src/tools/clippy/tests/ui/double_neg.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[warn(clippy::double_neg)]
#[allow(clippy::no_effect)]
fn main() {
    let x = 1;
    -x;
    -(-x);
    --x;
}


