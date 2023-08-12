tests/ui/binop/binop-logic-float.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() { let x = 1.0_f32 || 2.0_f32; }
//~^ ERROR mismatched types
//~| ERROR mismatched types


