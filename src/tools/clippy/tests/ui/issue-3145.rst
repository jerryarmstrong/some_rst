src/tools/clippy/tests/ui/issue-3145.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    println!("{}" a); //~ERROR expected `,`, found `a`
}


