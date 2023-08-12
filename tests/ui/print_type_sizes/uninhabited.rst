tests/ui/print_type_sizes/uninhabited.rs
========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -Z print-type-sizes --crate-type=lib
// build-pass
// ignore-pass
// ^-- needed because `--pass check` does not emit the output needed.
//     FIXME: consider using an attribute instead of side-effects.

#![feature(never_type)]

pub fn test() {
    let _x: Option<!> = None;
    let _y: Result<u32, !> = Ok(42);
    let _z: Result<!, !> = loop {};
}


