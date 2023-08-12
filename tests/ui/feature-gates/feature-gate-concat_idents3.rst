tests/ui/feature-gates/feature-gate-concat_idents3.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const XY_1: i32 = 10;

fn main() {
    const XY_2: i32 = 20;
    assert_eq!(10, concat_idents!(X, Y_1)); //~ ERROR `concat_idents` is not stable
    assert_eq!(20, concat_idents!(X, Y_2)); //~ ERROR `concat_idents` is not stable
}


