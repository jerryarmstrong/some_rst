tests/ui/hashmap/hashmap-lifetimes.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut my_stuff = std::collections::HashMap::new();
    my_stuff.insert(0, 42);

    let mut it = my_stuff.iter();
    my_stuff.insert(1, 43); //~ ERROR cannot borrow
    it;
}


