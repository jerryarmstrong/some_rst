tests/ui/match/match-unresolved-one-arm.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo<T>() -> T { panic!("Rocks for my pillow") }

fn main() {
    let x = match () { //~ ERROR type annotations needed
        () => foo() // T here should be unresolved
    };
}


