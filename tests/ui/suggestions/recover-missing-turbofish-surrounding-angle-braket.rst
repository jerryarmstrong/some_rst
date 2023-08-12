tests/ui/suggestions/recover-missing-turbofish-surrounding-angle-braket.rs
==========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let _ = vec![1, 2, 3].into_iter().collect::Vec<_>();
    //~^ ERROR generic parameters without surrounding angle brackets
    let _ = vec![1, 2, 3].into_iter().collect::Vec<_>>>>();
    //~^ ERROR generic parameters without surrounding angle brackets
    let _ = vec![1, 2, 3].into_iter().collect::Vec<_>>>();
    //~^ ERROR generic parameters without surrounding angle brackets
    let _ = vec![1, 2, 3].into_iter().collect::Vec<_>>();
    //~^ ERROR generic parameters without surrounding angle brackets
}


