tests/ui/borrowck/borrowck-init-op-equal.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test() {
    let v: isize;
    v += 1; //~ ERROR E0381
    v.clone();
}

fn main() {
}


