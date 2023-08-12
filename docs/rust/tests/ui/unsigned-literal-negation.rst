tests/ui/unsigned-literal-negation.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = -1 as usize; //~ ERROR: cannot apply unary operator `-`
    let x = (-1) as usize; //~ ERROR: cannot apply unary operator `-`
    let x: u32 = -1; //~ ERROR: cannot apply unary operator `-`
}


