tests/ui/traits/item-inside-macro.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Issue #34183

macro_rules! foo {
    () => {
        fn foo() { }
    }
}

macro_rules! bar {
    () => {
        fn bar();
    }
}

trait Bleh {
    foo!();
    bar!();
}

struct Test;

impl Bleh for Test {
    fn bar() {}
}

fn main() {
    Test::bar();
    Test::foo();
}


