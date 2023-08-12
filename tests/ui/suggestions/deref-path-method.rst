tests/ui/suggestions/deref-path-method.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let vec = Vec::new();
    Vec::contains(&vec, &0);
    //~^ ERROR no function or associated item named `contains` found for struct `Vec<_, _>` in the current scope
    //~| HELP the function `contains` is implemented on `[_]`
}


