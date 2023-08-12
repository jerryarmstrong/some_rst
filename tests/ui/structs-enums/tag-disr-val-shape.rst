tests/ui/structs-enums/tag-disr-val-shape.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

#[derive(Debug)]
enum color {
    red = 0xff0000,
    green = 0x00ff00,
    blue = 0x0000ff,
    black = 0x000000,
    white = 0xFFFFFF,
}

pub fn main() {
    let act = format!("{:?}", color::red);
    println!("{}", act);
    assert_eq!("red".to_string(), act);
    assert_eq!("green".to_string(), format!("{:?}", color::green));
    assert_eq!("white".to_string(), format!("{:?}", color::white));
}


