tests/ui/consts/const-needs_drop.rs
===================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

use std::mem;

#[allow(unused_tuple_struct_fields)]
struct Trivial(u8, f32);

#[allow(unused_tuple_struct_fields)]
struct NonTrivial(u8, String);

const CONST_U8: bool = mem::needs_drop::<u8>();
const CONST_STRING: bool = mem::needs_drop::<String>();
const CONST_TRIVIAL: bool = mem::needs_drop::<Trivial>();
const CONST_NON_TRIVIAL: bool = mem::needs_drop::<NonTrivial>();

static STATIC_U8: bool = mem::needs_drop::<u8>();
static STATIC_STRING: bool = mem::needs_drop::<String>();
static STATIC_TRIVIAL: bool = mem::needs_drop::<Trivial>();
static STATIC_NON_TRIVIAL: bool = mem::needs_drop::<NonTrivial>();

fn main() {
    assert!(!CONST_U8);
    assert!(CONST_STRING);
    assert!(!CONST_TRIVIAL);
    assert!(CONST_NON_TRIVIAL);

    assert!(!STATIC_U8);
    assert!(STATIC_STRING);
    assert!(!STATIC_TRIVIAL);
    assert!(STATIC_NON_TRIVIAL);
}


