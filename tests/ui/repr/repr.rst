tests/ui/repr/repr.rs
=====================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[repr] //~ ERROR malformed `repr` attribute
struct _A {}

#[repr = "B"] //~ ERROR malformed `repr` attribute
struct _B {}

#[repr = "C"] //~ ERROR malformed `repr` attribute
struct _C {}

#[repr(C)]
struct _D {}

fn main() {}


