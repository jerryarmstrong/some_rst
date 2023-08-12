tests/ui/consts/const-eval/const-eval-span.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that error in constant evaluation of enum discriminant
// provides the context for what caused the evaluation.

struct S(i32);

const CONSTANT: S = S(0);

enum E {
    V = CONSTANT,
    //~^ ERROR mismatched types
    //~| expected `isize`, found struct `S`
}

fn main() {}


