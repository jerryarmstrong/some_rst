tests/ui/expr/if/if-without-else-result.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let a = if true { true };
    //~^ ERROR `if` may be missing an `else` clause [E0317]
    //~| expected `bool`, found `()`
    println!("{}", a);
}


