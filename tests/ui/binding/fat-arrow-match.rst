tests/ui/binding/fat-arrow-match.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

enum color {
    red,
    green,
    blue
}

pub fn main() {
    println!("{}", match color::red {
        color::red => { 1 }
        color::green => { 2 }
        color::blue => { 3 }
    });
}


