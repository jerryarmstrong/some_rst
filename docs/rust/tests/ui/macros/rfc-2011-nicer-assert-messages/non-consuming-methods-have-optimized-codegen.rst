tests/ui/macros/rfc-2011-nicer-assert-messages/non-consuming-methods-have-optimized-codegen.rs
==============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass
// compile-flags: -Z unpretty=expanded

#![feature(core_intrinsics, generic_assert, generic_assert_internals)]

fn arbitrary_consuming_method_for_demonstration_purposes() {
    let elem = 1i32;
    assert!(elem as usize);
}

fn addr_of() {
    let elem = 1i32;
    assert!(&elem);
}

fn binary() {
    let elem = 1i32;
    assert!(elem == 1);
    assert!(elem >= 1);
    assert!(elem > 0);
    assert!(elem < 3);
    assert!(elem <= 3);
    assert!(elem != 3);
}

fn unary() {
    let elem = &1i32;
    assert!(*elem);
}

fn main() {
}


