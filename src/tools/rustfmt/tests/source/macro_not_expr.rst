src/tools/rustfmt/tests/source/macro_not_expr.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    macro_rules! test {
    ($($t:tt)*) => {}
}

fn main() {
    test!( a : B => c d );
}


