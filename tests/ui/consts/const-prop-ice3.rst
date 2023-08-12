tests/ui/consts/const-prop-ice3.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass (ensure that const-prop is run)

struct A<T: ?Sized>(T);

fn main() {
    let _x = &(&A([2, 3]) as &A<[i32]>).0 as *const [i32] as *const i32;
}


