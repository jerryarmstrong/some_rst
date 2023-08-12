tests/ui/consts/mir_check_nonconst.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![allow(dead_code)]

struct Foo { a: u8 }
fn bar() -> Foo {
    Foo { a: 5 }
}

static foo: Foo = bar();
//~^ ERROR cannot call non-const fn

fn main() {}


