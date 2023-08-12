tests/ui/parser/suggest-const-for-global-var.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    let X: i32 = 12;
//~^ ERROR expected item, found keyword `let`

fn main() {
    println!("{}", X);
}


