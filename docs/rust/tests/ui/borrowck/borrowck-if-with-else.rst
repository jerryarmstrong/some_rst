tests/ui/borrowck/borrowck-if-with-else.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: isize) { println!("{}", x); }

fn main() {
    let x: isize;
    if 1 > 2 {
        println!("whoops");
    } else {
        x = 10;
    }
    foo(x); //~ ERROR E0381
}


