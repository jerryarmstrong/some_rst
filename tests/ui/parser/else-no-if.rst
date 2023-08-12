tests/ui/parser/else-no-if.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() {
    if true {
    } else false {
    //~^ ERROR expected `{`, found keyword `false`
    }
}

fn foo2() {
    if true {
    } else falsy() {
    //~^ ERROR expected `{`, found `falsy`
    }
}

fn foo3() {
    if true {
    } else falsy();
    //~^ ERROR expected `{`, found `falsy`
}

fn foo4() {
    if true {
    } else loop{}
    //~^ ERROR expected `{`, found keyword `loop`
    {}
}

fn falsy() -> bool {
    false
}

fn main() {}


