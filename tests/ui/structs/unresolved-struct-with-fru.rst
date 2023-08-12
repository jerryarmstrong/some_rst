tests/ui/structs/unresolved-struct-with-fru.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S {
    a: u32,
}

fn main() {
    let s1 = S { a: 1 };

    let _ = || {
        let s2 = Oops { a: 2, ..s1 };
        //~^ ERROR cannot find struct, variant or union type `Oops` in this scope
    };
}


