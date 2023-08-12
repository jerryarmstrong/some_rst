tests/ui/parser/keywords-followed-by-double-colon.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    struct::foo();
    //~^ ERROR expected identifier
}
fn bar() {
    mut::baz();
    //~^ ERROR expected expression, found keyword `mut`
}


