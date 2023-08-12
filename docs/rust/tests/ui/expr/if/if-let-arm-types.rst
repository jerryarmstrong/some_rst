tests/ui/expr/if/if-let-arm-types.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    if let Some(b) = None {
        //~^ NOTE `if` and `else` have incompatible types
        ()
        //~^ NOTE expected because of this
    } else {
        1
    };
    //~^^ ERROR: `if` and `else` have incompatible types
    //~| NOTE expected `()`, found integer
}


