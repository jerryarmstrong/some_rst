src/tools/clippy/tests/ui/if_not_else.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![warn(clippy::all)]
#![warn(clippy::if_not_else)]

fn foo() -> bool {
    unimplemented!()
}
fn bla() -> bool {
    unimplemented!()
}

fn main() {
    if !bla() {
        println!("Bugs");
    } else {
        println!("Bunny");
    }
    if 4 != 5 {
        println!("Bugs");
    } else {
        println!("Bunny");
    }
    if !foo() {
        println!("Foo");
    } else if !bla() {
        println!("Bugs");
    } else {
        println!("Bunny");
    }
}


