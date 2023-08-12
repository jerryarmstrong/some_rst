tests/ui/borrowck/borrowck-use-in-index-lvalue.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test() {
    let w: &mut [isize];
    w[5] = 0; //~ ERROR [E0381]

    let mut w: &mut [isize];
    w[5] = 0; //~ ERROR [E0381]
}

fn main() { test(); }


