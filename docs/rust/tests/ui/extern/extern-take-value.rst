tests/ui/extern/extern-take-value.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// aux-build:extern-take-value.rs

extern crate extern_take_value;

pub fn main() {
    let a: extern "C" fn() -> i32 = extern_take_value::get_f();
    let b: extern "C" fn() -> i32 = extern_take_value::get_f();
    let c: extern "C" fn() -> i32 = extern_take_value::get_g();

    assert!(a == b);
    assert!(a != c);
}


