tests/ui/structs/struct-pat-derived-error.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct A {
    b: usize,
    c: usize
}

impl A {
    fn foo(&self) {
        let A { x, y } = self.d; //~ ERROR no field `d` on type `&A`
        //~^ ERROR struct `A` does not have fields named `x`, `y`
        //~| ERROR pattern does not mention fields `b`, `c`
    }
}

fn main() {}


