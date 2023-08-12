tests/ui/closures/add_semicolon_non_block_closure.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(_f: impl Fn()) {}

fn bar() -> i32 {
    1
}

fn main() {
    foo(|| bar())
    //~^ ERROR mismatched types [E0308]
    //~| HELP consider using a semicolon here
}


