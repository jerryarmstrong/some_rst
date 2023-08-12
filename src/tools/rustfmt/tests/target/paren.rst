src/tools/rustfmt/tests/target/paren.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x = (1);
    let y = (/* comment */(2));
    let z = ((3)/* comment */);
    let a = (4/* comment */);
}


