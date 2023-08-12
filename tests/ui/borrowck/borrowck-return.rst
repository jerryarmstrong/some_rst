tests/ui/borrowck/borrowck-return.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() -> isize {
    let x: isize;
    return x; //~ ERROR E0381
}

fn main() { f(); }


