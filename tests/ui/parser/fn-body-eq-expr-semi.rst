tests/ui/parser/fn-body-eq-expr-semi.rs
=======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

fn syntax() {
    fn foo() = 42; //~ ERROR function body cannot be `= expression;`
    fn bar() -> u8 = 42; //~ ERROR function body cannot be `= expression;`
}

extern "C" {
    fn foo() = 42; //~ ERROR function body cannot be `= expression;`
    //~^ ERROR incorrect function inside `extern` block
    fn bar() -> u8 = 42; //~ ERROR function body cannot be `= expression;`
    //~^ ERROR incorrect function inside `extern` block
}

trait Foo {
    fn foo() = 42; //~ ERROR function body cannot be `= expression;`
    fn bar() -> u8 = 42; //~ ERROR function body cannot be `= expression;`
}

impl Foo for () {
    fn foo() = 42; //~ ERROR function body cannot be `= expression;`
    fn bar() -> u8 = 42; //~ ERROR function body cannot be `= expression;`
}


