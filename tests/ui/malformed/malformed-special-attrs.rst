tests/ui/malformed/malformed-special-attrs.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #[cfg_attr] //~ ERROR malformed `cfg_attr` attribute
struct S1;

#[cfg_attr = ""] //~ ERROR malformed `cfg_attr` attribute
struct S2;

#[derive] //~ ERROR malformed `derive` attribute
struct S3;

#[derive = ""] //~ ERROR malformed `derive` attribute
struct S4;

fn main() {}


