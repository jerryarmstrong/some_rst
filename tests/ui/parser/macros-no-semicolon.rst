tests/ui/parser/macros-no-semicolon.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    assert_eq!(1, 2) //~ ERROR: expected `;`
    assert_eq!(3, 4) //~ ERROR: expected `;`
    println!("hello");
}


