tests/ui/parser/unnecessary-let.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    for let x of [1, 2, 3] {}
    //~^ ERROR expected pattern, found `let`
    //~| ERROR missing `in` in `for` loop

    match 1 {
        let 1 => {}
        //~^ ERROR expected pattern, found `let`
        _ => {}
    }
}


