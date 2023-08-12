tests/ui/derives/derives-span-PartialOrd-tuple-struct.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-deriving-span-tests.py'

#[derive(PartialEq)]
struct Error;

#[derive(PartialOrd,PartialEq)]
struct Struct(
    Error //~ ERROR can't compare `Error` with `Error`
);

fn main() {}


