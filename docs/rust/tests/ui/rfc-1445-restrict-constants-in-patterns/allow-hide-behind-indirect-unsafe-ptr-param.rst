tests/ui/rfc-1445-restrict-constants-in-patterns/allow-hide-behind-indirect-unsafe-ptr-param.rs
===============================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test explores how `#[structral_match]` behaves in tandem with
// `*const` and `*mut` pointers.

// run-pass

#![warn(pointer_structural_match)]

struct NoDerive(#[allow(unused_tuple_struct_fields)] i32);

// This impl makes NoDerive irreflexive
// (which doesn't matter here because `<*const T>::eq` won't recur on `T`).
impl PartialEq for NoDerive { fn eq(&self, _: &Self) -> bool { false } }

impl Eq for NoDerive { }

#[derive(PartialEq, Eq)]
struct WrapParam<X>(*const X);

const WRAP_UNSAFE_PARAM: & &WrapParam<NoDerive> = & &WrapParam(std::ptr::null());

fn main() {
    match WRAP_UNSAFE_PARAM {
        WRAP_UNSAFE_PARAM => { println!("WRAP_UNSAFE_PARAM correctly matched itself"); }
        _ => { panic!("WRAP_UNSAFE_PARAM did not match itself"); }
    }
}


