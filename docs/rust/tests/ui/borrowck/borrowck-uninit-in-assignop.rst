tests/ui/borrowck/borrowck-uninit-in-assignop.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Tests that the use of uninitialized variable in assignment operator
// expression is detected.

pub fn main() {
    let x: isize;
    x += 1; //~ ERROR E0381

    let x: isize;
    x -= 1; //~ ERROR E0381

    let x: isize;
    x *= 1; //~ ERROR E0381

    let x: isize;
    x /= 1; //~ ERROR E0381

    let x: isize;
    x %= 1; //~ ERROR E0381

    let x: isize;
    x ^= 1; //~ ERROR E0381

    let x: isize;
    x &= 1; //~ ERROR E0381

    let x: isize;
    x |= 1; //~ ERROR E0381

    let x: isize;
    x <<= 1; //~ ERROR E0381

    let x: isize;
    x >>= 1; //~ ERROR E0381
}


