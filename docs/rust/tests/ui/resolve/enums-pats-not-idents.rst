tests/ui/resolve/enums-pats-not-idents.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a(1) = 13; //~ ERROR cannot find tuple struct or tuple variant `a` in this scope
}


