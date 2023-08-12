tests/ui/consts/const-eval/conditional_array_execution.rs
=========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const X: u32 = 5;
const Y: u32 = 6;
const FOO: u32 = [X - Y, Y - X][(X < Y) as usize];
//~^ ERROR constant

fn main() {
    println!("{}", FOO);
}


