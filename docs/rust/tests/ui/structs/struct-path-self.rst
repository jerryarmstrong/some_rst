tests/ui/structs/struct-path-self.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;

trait Tr {
    fn f() {
        let s = Self {};
        //~^ ERROR expected struct, variant or union type, found type parameter
        let z = Self::<u8> {};
        //~^ ERROR expected struct, variant or union type, found type parameter
        //~| ERROR type arguments are not allowed on self type
        match s {
            Self { .. } => {}
            //~^ ERROR expected struct, variant or union type, found type parameter
        }
    }
}

impl Tr for S {
    fn f() {
        let s = Self {}; // OK
        let z = Self::<u8> {}; //~ ERROR type arguments are not allowed on self type
        match s {
            Self { .. } => {} // OK
        }
    }
}

impl S {
    fn g() {
        let s = Self {}; // OK
        let z = Self::<u8> {}; //~ ERROR type arguments are not allowed on self type
        match s {
            Self { .. } => {} // OK
        }
    }
}

fn main() {}


