tests/ui/structs-enums/simple-match-generic-tag.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

enum opt<T> { none, some(T) }

pub fn main() {
    let x = opt::none::<isize>;
    match x {
        opt::none::<isize> => { println!("hello world"); }
        opt::some(_) => { }
    }
}


