tests/ui/where-clauses/ignore-err-clauses.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    use std::ops::Add;

fn dbl<T>(x: T) -> <T as Add>::Output
where
    T: Copy + Add,
    UUU: Copy,
    //~^ ERROR cannot find type `UUU` in this scope
{
    x + x
}

fn main() {
    println!("{}", dbl(3));
}


