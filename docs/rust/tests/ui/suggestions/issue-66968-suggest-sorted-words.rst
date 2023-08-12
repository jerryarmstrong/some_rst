tests/ui/suggestions/issue-66968-suggest-sorted-words.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a_longer_variable_name = 1;
    println!("{}", a_variable_longer_name); //~ ERROR E0425
}


