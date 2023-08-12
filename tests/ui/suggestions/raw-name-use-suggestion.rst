tests/ui/suggestions/raw-name-use-suggestion.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    mod foo {
    pub fn r#let() {}
    pub fn break() {} //~ ERROR expected identifier, found keyword `break`
}

fn main() {
    foo::let(); //~ ERROR expected identifier, found keyword `let`
    r#break(); //~ ERROR cannot find function `r#break` in this scope
}


