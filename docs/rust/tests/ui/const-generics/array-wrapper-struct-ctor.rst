tests/ui/const-generics/array-wrapper-struct-ctor.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

#![allow(dead_code)]

struct ArrayStruct<T, const N: usize> {
    data: [T; N],
}

struct ArrayTuple<T, const N: usize>([T; N]);

fn main() {
    let _ = ArrayStruct { data: [0u32; 8] };
    let _ = ArrayTuple([0u32; 8]);
}


