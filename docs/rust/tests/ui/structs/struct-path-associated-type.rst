tests/ui/structs/struct-path-associated-type.rs
===============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;

trait Tr {
    type A;
}

impl Tr for S {
    type A = S;
}

fn f<T: Tr>() {
    let s = T::A {};
    //~^ ERROR expected struct, variant or union type, found associated type
    let z = T::A::<u8> {};
    //~^ ERROR expected struct, variant or union type, found associated type
    //~| ERROR this associated type takes 0 generic arguments but 1 generic argument was supplied
    match S {
        T::A {} => {}
        //~^ ERROR expected struct, variant or union type, found associated type
    }
}

fn g<T: Tr<A = S>>() {
    let s = T::A {}; // OK
    let z = T::A::<u8> {}; //~ ERROR this associated type takes 0 generic arguments but 1 generic argument was supplied
    match S {
        T::A {} => {} // OK
    }
}

fn main() {
    let s = S::A {}; //~ ERROR ambiguous associated type
    let z = S::A::<u8> {}; //~ ERROR ambiguous associated type
    match S {
        S::A {} => {} //~ ERROR ambiguous associated type
    }
}


