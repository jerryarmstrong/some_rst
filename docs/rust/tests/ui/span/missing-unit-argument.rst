tests/ui/span/missing-unit-argument.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(():(), ():()) {}
fn bar(():()) {}

struct S;
impl S {
    fn baz(self, (): ()) { }
    fn generic<T>(self, _: T) { }
}

fn main() {
    let _: Result<(), String> = Ok(); //~ ERROR this enum variant takes
    foo(); //~ ERROR function takes
    foo(()); //~ ERROR function takes
    bar(); //~ ERROR function takes
    S.baz(); //~ ERROR this method takes
    S.generic::<()>(); //~ ERROR this method takes
}


