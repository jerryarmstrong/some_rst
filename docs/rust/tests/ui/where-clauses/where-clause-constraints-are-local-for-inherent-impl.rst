tests/ui/where-clauses/where-clause-constraints-are-local-for-inherent-impl.rs
==============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn require_copy<T: Copy>(x: T) {}

struct Foo<T> { x: T }

// Ensure constraints are only attached to methods locally
impl<T> Foo<T> {
    fn needs_copy(self) where T: Copy {
        require_copy(self.x);

    }

    fn fails_copy(self) {
        require_copy(self.x);
        //~^ ERROR the trait bound `T: Copy` is not satisfied
    }
}

fn main() {}


