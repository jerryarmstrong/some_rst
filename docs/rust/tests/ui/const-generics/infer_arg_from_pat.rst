tests/ui/const-generics/infer_arg_from_pat.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
//
// see issue #70529

struct A<const N: usize> {
    arr: [u8; N],
}

impl<const N: usize> A<N> {
    fn new() -> Self {
        A {
            arr: [0; N],
        }
    }

    fn value(&self) -> usize {
        N
    }
}

fn main() {
    let a = A::new();
    let [_, _] = a.arr;
    assert_eq!(a.value(), 2);
}


