tests/ui/where-clauses/where-clauses-method-unsatisfied.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a where clause attached to a method allows us to add
// additional constraints to a parameter out of scope.

struct Foo<T> {
    value: T
}

struct Bar; // does not implement Eq

impl<T> Foo<T> {
    fn equals(&self, u: &Foo<T>) -> bool where T : Eq {
        self.value == u.value
    }
}

fn main() {
    let x = Foo { value: Bar };
    x.equals(&x);
    //~^ ERROR `Bar: Eq` is not satisfied
}


