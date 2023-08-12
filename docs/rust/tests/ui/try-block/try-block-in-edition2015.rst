tests/ui/try-block/try-block-in-edition2015.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: --edition 2015

pub fn main() {
    let try_result: Option<_> = try {
    //~^ ERROR expected struct, variant or union type, found macro `try`
        let x = 5; //~ ERROR expected identifier, found keyword
        x
    };
    assert_eq!(try_result, Some(5));
}


