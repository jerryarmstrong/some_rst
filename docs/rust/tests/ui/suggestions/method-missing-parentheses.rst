tests/ui/suggestions/method-missing-parentheses.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = vec![].into_iter().collect::<usize>;
    //~^ ERROR attempted to take value of method `collect` on type `std::vec::IntoIter<_>`
    //~| ERROR field expressions cannot have generic arguments
}


