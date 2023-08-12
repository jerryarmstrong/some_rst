tests/ui/extern/extern-thiscall.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// only-x86

#![feature(abi_thiscall)]

trait A {
    extern "thiscall" fn test1(i: i32);
}

struct S;

impl A for S {
    extern "thiscall" fn test1(i: i32) {
        assert_eq!(i, 1);
    }
}

extern "thiscall" fn test2(i: i32) {
    assert_eq!(i, 2);
}

fn main() {
    <S as A>::test1(1);
    test2(2);
}


