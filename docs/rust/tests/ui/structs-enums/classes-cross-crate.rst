tests/ui/structs-enums/classes-cross-crate.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:cci_class_4.rs

extern crate cci_class_4;
use cci_class_4::kitties::cat;

pub fn main() {
    let mut nyan = cat(0_usize, 2, "nyan".to_string());
    nyan.eat();
    assert!((!nyan.eat()));
    for _ in 1_usize..10_usize { nyan.speak(); };
    assert!((nyan.eat()));
}


