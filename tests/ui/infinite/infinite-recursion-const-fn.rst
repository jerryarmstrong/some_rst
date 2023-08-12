tests/ui/infinite/infinite-recursion-const-fn.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    //https://github.com/rust-lang/rust/issues/31364

const fn a() -> usize {
    b() //~ ERROR evaluation of constant value failed [E0080]
}
const fn b() -> usize {
    a()
}
const ARR: [i32; a()] = [5; 6];

fn main() {}


