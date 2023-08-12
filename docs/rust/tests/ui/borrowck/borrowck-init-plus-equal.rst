tests/ui/borrowck/borrowck-init-plus-equal.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test() {
    let mut v: isize;
    v = v + 1; //~ ERROR E0381
    v.clone();
}

fn main() {
}


