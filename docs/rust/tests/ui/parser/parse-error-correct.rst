tests/ui/parser/parse-error-correct.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that the parser is error correcting missing idents. Despite a parsing
// error (or two), we still run type checking (and don't get extra errors there).

fn main() {
    let y = 42;
    let x = y.;  //~ ERROR unexpected token
    let x = y.();  //~ ERROR unexpected token
                   //~^ ERROR expected function, found `{integer}`
    let x = y.foo; //~ ERROR `{integer}` is a primitive type and therefore doesn't have fields [E061
}


