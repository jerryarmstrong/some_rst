tests/ui/issues/issue-2951.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T, U>(x: T, y: U) {
    let mut xx = x;
    xx = y;
    //~^  ERROR mismatched types
    //~| expected type parameter `T`, found type parameter `U`
    //~| expected type parameter `T`
    //~| found type parameter `U`
}

fn main() {
}


