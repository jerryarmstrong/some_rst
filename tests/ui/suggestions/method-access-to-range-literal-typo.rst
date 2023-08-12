tests/ui/suggestions/method-access-to-range-literal-typo.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-rustfix

#![allow(unused)]

fn as_ref() -> Option<Vec<u8>> {
    None
}
struct Type {
    option: Option<Vec<u8>>
}
trait Trait {
    fn foo(&self) -> &Vec<u8>;
}
impl Trait for Option<Vec<u8>> {
    fn foo(&self) -> &Vec<u8> {
        self.as_ref().unwrap()
    }
}

impl Type {
    fn method(&self) -> Option<&Vec<u8>> {
        self.option..as_ref().map(|x| x)
        //~^ ERROR E0308
    }
    fn method2(&self) -> Option<&u8> {
        self.option..foo().get(0)
        //~^ ERROR E0425
        //~| ERROR E0308
    }
}

fn main() {
    let _ = Type { option: None }.method();
}


