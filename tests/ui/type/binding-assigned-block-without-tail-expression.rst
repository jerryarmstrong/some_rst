tests/ui/type/binding-assigned-block-without-tail-expression.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct S;
fn main() {
    let x = {
        println!("foo");
        42;
    };
    let y = {};
    let z = {
        "hi";
    };
    let s = {
        S;
    };
    println!("{}", x); //~ ERROR E0277
    println!("{}", y); //~ ERROR E0277
    println!("{}", z); //~ ERROR E0277
    println!("{}", s); //~ ERROR E0277
    let _: i32 = x; //~ ERROR E0308
    let _: i32 = y; //~ ERROR E0308
    let _: i32 = z; //~ ERROR E0308
    let _: i32 = s; //~ ERROR E0308
}


