tests/ui/parser/parser-recovery-2.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that we can recover from mismatched braces in the parser.

trait Foo {
    fn bar() {
        let x = foo(); //~ ERROR cannot find function `foo` in this scope
    ) //~ ERROR mismatched closing delimiter: `)`
}

fn main() {
    let x = y.;  //~ ERROR unexpected token
                 //~^ ERROR cannot find value `y` in this scope
}


