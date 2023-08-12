tests/ui/parser/if-in-in.rs
===========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

fn main() {
    for i in in 1..2 { //~ ERROR expected iterable, found keyword `in`
        println!("{}", i);
    }
}


