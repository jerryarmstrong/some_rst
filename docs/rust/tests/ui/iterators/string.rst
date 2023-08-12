tests/ui/iterators/string.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for _ in "".to_owned() {}
    //~^ ERROR `String` is not an iterator
    for _ in "" {}
    //~^ ERROR `&str` is not an iterator
}


