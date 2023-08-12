tests/ui/structs-enums/rec-auto.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass




// Issue #50.

struct X { foo: String, bar: String }

pub fn main() {
    let x = X {foo: "hello".to_string(), bar: "world".to_string()};
    println!("{}", x.foo.clone());
    println!("{}", x.bar.clone());
}


