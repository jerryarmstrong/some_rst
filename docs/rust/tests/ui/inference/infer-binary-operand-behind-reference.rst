tests/ui/inference/infer-binary-operand-behind-reference.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn main() {
    // Test that we can infer the type of binary operands when
    // references are involved, on various types and operators.
    let _: u8 = 0 + 0;
    let _: u8 = 0 + &0;
    let _: u8 = &0 + 0;
    let _: u8 = &0 + &0;

    let _: f32 = 0.0 + 0.0;
    let _: f32 = 0.0 + &0.0;
    let _: f32 = &0.0 + 0.0;
    let _: f32 = &0.0 + &0.0;

    let _: u8 = 0 << 0;
    let _: u8 = 0 << &0;
    let _: u8 = &0 << 0;
    let _: u8 = &0 << &0;

    // Test type inference when variable types are indirectly inferred.
    let a = 22;
    let _: usize = a + &44;

    // When we have no expected type, the types of the operands is the default type.
    let _ = 0 + 0;
    let _ = 0 + &0;
    let _ = &0 + 0;
    let _ = &0 + &0;
}


