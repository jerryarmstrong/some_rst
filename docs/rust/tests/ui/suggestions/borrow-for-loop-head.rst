tests/ui/suggestions/borrow-for-loop-head.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = vec![1, 2, 3];
    for i in &a {
        for j in a {
        //~^ ERROR cannot move out of `a` because it is borrowed
        //~| ERROR use of moved value: `a`
            println!("{} * {} = {}", i, j, i * j);
        }
    }
}


