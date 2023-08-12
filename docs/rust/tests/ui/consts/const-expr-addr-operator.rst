tests/ui/consts/const-expr-addr-operator.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Encountered while testing #44614.
// build-pass (FIXME(62277): could be check-pass?)

pub fn main() {
    // Constant of generic type (int)
    const X: &'static u32 = &22;
    assert_eq!(0, match &22 {
        X => 0,
        _ => 1,
    });
}


