tests/ui/consts/ct-var-in-collect_all_mismatches.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Foo<T, const N: usize> {
    array: [T; N],
}

trait Bar<const N: usize> {}

impl<T, const N: usize> Foo<T, N> {
    fn trigger(self) {
        self.unsatisfied()
        //~^ ERROR the trait bound `T: Bar<N>` is not satisfied
    }

    fn unsatisfied(self)
    where
        T: Bar<N>,
    {
    }
}

fn main() {}


