tests/ui/consts/const-as-fn.rs
==============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    const FOO: usize = 0;

fn main() {
    FOO(); //~ ERROR expected function, found `usize`
}


