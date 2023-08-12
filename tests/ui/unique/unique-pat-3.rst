tests/ui/unique/unique-pat-3.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

enum bar { u(Box<isize>), w(isize), }

pub fn main() {
    let v = match bar::u(10.into()) {
        bar::u(a) => {
            println!("{}", a);
            *a
        }
        _ => { 66 }
    };
    assert_eq!(v, 10);
}


