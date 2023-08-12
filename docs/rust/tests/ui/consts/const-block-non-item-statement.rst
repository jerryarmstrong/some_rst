tests/ui/consts/const-block-non-item-statement.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

enum Foo {
    Bar = { let x = 1; 3 }
}


const A: usize = { 1; 2 };

const B: usize = { { } 2 };

macro_rules! foo {
    () => (())
}

const C: usize = { foo!(); 2 };

const D: usize = { let x = 4; 2 };

type Array = [u32; {  let x = 2; 5 }];
type Array2 = [u32; { let mut x = 2; x = 3; x}];

pub fn main() {}


