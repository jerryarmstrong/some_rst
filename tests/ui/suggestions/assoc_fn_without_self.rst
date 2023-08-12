tests/ui/suggestions/assoc_fn_without_self.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {}

struct S;

impl S {
    fn foo() {}

    fn bar(&self) {}

    fn baz(a: u8, b: u8) {}

    fn b() {
        fn c() {
            foo(); //~ ERROR cannot find function `foo` in this scope
        }
        foo(); //~ ERROR cannot find function `foo` in this scope
        bar(); //~ ERROR cannot find function `bar` in this scope
        baz(2, 3); //~ ERROR cannot find function `baz` in this scope
    }
}


