tests/ui/consts/self_normalization2.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

trait Gen<T> {
    fn gen(x: Self) -> T;
}

struct A;

impl Gen<[(); 0]> for A {
    fn gen(x: Self) -> [(); 0] {
        []
    }
}

fn array() -> impl Gen<[(); 0]> {
    A
}

fn main() {
    let [] = Gen::gen(array());
}


