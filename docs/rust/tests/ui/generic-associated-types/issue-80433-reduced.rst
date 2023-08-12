tests/ui/generic-associated-types/issue-80433-reduced.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

struct E {}

trait TestMut {
    type Output<'a>;
    fn test_mut(&mut self) -> Self::Output<'static>;
}

impl TestMut for E {
    type Output<'a> = usize;
    fn test_mut(&mut self) -> Self::Output<'static> {
        todo!()
    }
}

fn test_simpler<'a>(_: impl TestMut<Output<'a> = usize>) {}

fn main() {
    test_simpler(E {});
}


