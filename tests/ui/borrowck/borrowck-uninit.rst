tests/ui/borrowck/borrowck-uninit.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(x: isize) { println!("{}", x); }

fn main() {
    let x: isize;
    foo(x); //~ ERROR E0381
}


