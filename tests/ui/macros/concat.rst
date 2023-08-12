tests/ui/macros/concat.rs
=========================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    concat!(b'f');  //~ ERROR: cannot concatenate a byte string literal
    concat!(b"foo");  //~ ERROR: cannot concatenate a byte string literal
    concat!(foo);   //~ ERROR: expected a literal
    concat!(foo()); //~ ERROR: expected a literal
}


