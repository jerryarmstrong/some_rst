tests/ui/assign-imm-local-twice.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test() {
    let v: isize;
    //~^ HELP consider making this binding mutable
    //~| SUGGESTION mut v
    v = 1; //~ NOTE first assignment
    println!("v={}", v);
    v = 2; //~ ERROR cannot assign twice to immutable variable
           //~| NOTE cannot assign twice to immutable
    println!("v={}", v);
}

fn main() {
}


