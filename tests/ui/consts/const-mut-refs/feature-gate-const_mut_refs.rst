tests/ui/consts/const-mut-refs/feature-gate-const_mut_refs.rs
=============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    foo(&mut 5);
}

const fn foo(x: &mut i32) -> i32 { //~ ERROR mutable references
    *x + 1

}


