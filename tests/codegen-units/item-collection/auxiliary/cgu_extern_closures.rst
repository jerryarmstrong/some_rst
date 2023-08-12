tests/codegen-units/item-collection/auxiliary/cgu_extern_closures.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![crate_type = "lib"]

#[inline]
pub fn inlined_fn(x: i32, y: i32) -> i32 {

    let closure = |a, b| { a + b };

    closure(x, y)
}

pub fn inlined_fn_generic<T>(x: i32, y: i32, z: T) -> (i32, T) {

    let closure = |a, b| { a + b };

    (closure(x, y), z)
}

pub fn non_inlined_fn(x: i32, y: i32) -> i32 {

    let closure = |a, b| { a + b };

    closure(x, y)
}


