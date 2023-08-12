tests/ui/borrowck/borrowck-for-loop-uninitialized-binding.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn f() -> isize {
    let mut x: isize;
    for _ in 0..0 { x = 10; }
    return x; //~ ERROR E0381
}

fn main() { f(); }


