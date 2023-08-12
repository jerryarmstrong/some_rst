tests/ui/parser/suggest-assoc-const.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Issue: 101797, Suggest associated const for incorrect use of let in traits
// run-rustfix
trait Trait {
    let _X: i32;
    //~^ ERROR non-item in item list
}

fn main() {

}


