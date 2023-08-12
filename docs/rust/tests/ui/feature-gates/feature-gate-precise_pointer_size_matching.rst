tests/ui/feature-gates/feature-gate-precise_pointer_size_matching.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    match 0usize {
        //~^ ERROR non-exhaustive patterns: `_` not covered
        //~| NOTE pattern `_` not covered
        //~| NOTE the matched value is of type `usize`
        //~| NOTE `usize` does not have a fixed maximum value
        0..=usize::MAX => {}
    }

    match 0isize {
        //~^ ERROR non-exhaustive patterns: `_` not covered
        //~| NOTE pattern `_` not covered
        //~| NOTE the matched value is of type `isize`
        //~| NOTE `isize` does not have a fixed maximum value
        isize::MIN..=isize::MAX => {}
    }
}


