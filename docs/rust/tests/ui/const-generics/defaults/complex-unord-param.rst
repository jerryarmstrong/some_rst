tests/ui/const-generics/defaults/complex-unord-param.rs
=======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Checks a complicated usage of unordered params
#![allow(dead_code)]

struct NestedArrays<'a, const N: usize, A: 'a, const M: usize, T:'a =u32> {
    args: &'a [&'a [T; M]; N],
    specifier: A,
}

fn main() {
    let array = [1, 2, 3];
    let nest = [&array];
    let _ = NestedArrays {
        args: &nest,
        specifier: true,
    };
}


