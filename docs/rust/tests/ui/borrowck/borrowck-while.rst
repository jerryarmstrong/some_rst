tests/ui/borrowck/borrowck-while.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() -> isize {
    let mut x: isize;
    while 1 == 1 { x = 10; }
    return x; //~ ERROR E0381
}

fn main() { f(); }


