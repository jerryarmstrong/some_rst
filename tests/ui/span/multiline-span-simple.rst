tests/ui/span/multiline-span-simple.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(a: u32, b: u32) {
    a + b;
}

fn bar(a: u32, b: u32) {
    a + b;
}

fn main() {
    let x = 1;
    let y = 2;
    let z = 3;
    foo(1 as u32 + //~ ERROR cannot add `()` to `u32`

        bar(x,

            y),

        z)
}


