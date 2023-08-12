tests/ui/destructuring-assignment/bad-expr-lhs.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    1 = 2; //~ ERROR invalid left-hand side of assignment
    1 += 2; //~ ERROR invalid left-hand side of assignment
    (1, 2) = (3, 4);
    //~^ ERROR invalid left-hand side of assignment
    //~| ERROR invalid left-hand side of assignment

    None = Some(3); //~ ERROR invalid left-hand side of assignment
}


