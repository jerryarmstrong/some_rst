tests/ui/argument-suggestions/extern-fn-arg-names.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    extern "Rust" {
    fn dstfn(src: i32, dst: err);
    //~^ ERROR cannot find type `err` in this scope
}

fn main() {
    dstfn(1);
    //~^ ERROR function takes 2 arguments but 1 argument was supplied
}


