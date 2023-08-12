tests/ui/const-generics/min_const_generics/inferred_const.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(generic_arg_infer)]
// run-pass

fn foo<const N: usize, const K: usize>(_data: [u32; N]) -> [u32; K] {
    [0; K]
}
fn main() {
    let _a = foo::<_, 2>([0, 1, 2]);
}


