tests/ui/suggestions/do-not-attempt-to-add-suggestions-with-no-changes.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::result;
impl result { //~ ERROR expected type, found module `result`
    fn into_future() -> Err {} //~ ERROR expected type, found variant `Err`
}
fn main() {}


