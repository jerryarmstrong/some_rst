tests/ui/lint/unused/must_use-tuple.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![deny(unused_must_use)]

fn foo() -> (Result<(), ()>, ()) {
    (Ok::<(), ()>(()), ())
}

fn main() {
    (Ok::<(), ()>(()),); //~ ERROR unused `Result`

    (Ok::<(), ()>(()), 0, Ok::<(), ()>(()), 5);
    //~^ ERROR unused `Result`
    //~^^ ERROR unused `Result`

    foo(); //~ ERROR unused `Result`

    ((Err::<(), ()>(()), ()), ()); //~ ERROR unused `Result`
}


