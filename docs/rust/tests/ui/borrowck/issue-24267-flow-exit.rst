tests/ui/borrowck/issue-24267-flow-exit.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Ensure that we reject code when a nonlocal exit (`break`,
// `continue`) causes us to pop over a needed assignment.

pub fn main() {
    foo1();
    foo2();
}

pub fn foo1() {
    let x: i32;
    loop { x = break; }
    println!("{}", x); //~ ERROR E0381
}

pub fn foo2() {
    let x: i32;
    for _ in 0..10 { x = continue; }
    println!("{}", x); //~ ERROR E0381
}


