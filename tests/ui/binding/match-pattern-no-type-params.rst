tests/ui/binding/match-pattern-no-type-params.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

enum maybe<T> { nothing, just(T), }

fn foo(x: maybe<isize>) {
    match x {
        maybe::nothing => { println!("A"); }
        maybe::just(_a) => { println!("B"); }
    }
}

pub fn main() { }


