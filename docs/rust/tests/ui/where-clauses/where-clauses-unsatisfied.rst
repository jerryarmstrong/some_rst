tests/ui/where-clauses/where-clauses-unsatisfied.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn equal<T>(a: &T, b: &T) -> bool where T : Eq { a == b }

struct Struct;

fn main() {
    drop(equal(&Struct, &Struct))
    //~^ ERROR the trait bound `Struct: Eq` is not satisfied
}


