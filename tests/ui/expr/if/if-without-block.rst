tests/ui/expr/if/if-without-block.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let n = 1;
    if 5 == {
    //~^ ERROR this `if` expression is missing a block after the condition
        println!("five");
    }
}


