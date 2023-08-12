tests/ui/const-generics/min_const_generics/const-evaluatable-unchecked.rs
=========================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Zdeduplicate-diagnostics=yes
#![allow(dead_code)]

fn foo<T>() {
    [0; std::mem::size_of::<*mut T>()];
    //~^ WARN cannot use constants which depend on generic parameters in types
    //~| WARN this was previously accepted by the compiler but is being phased out
}

struct Foo<T>(T);

impl<T> Foo<T> {
    const ASSOC: usize = 4;

    fn test() {
        let _ = [0; Self::ASSOC];
        //~^ WARN cannot use constants which depend on generic parameters in types
        //~| WARN this was previously accepted by the compiler but is being phased out
    }
}

struct Bar<const N: usize>;

impl<const N: usize> Bar<N> {
    const ASSOC: usize = 4;

    fn test() {
        let _ = [0; Self::ASSOC];
        //~^ WARN cannot use constants which depend on generic parameters in types
        //~| WARN this was previously accepted by the compiler but is being phased out
    }
}

fn main() {}


