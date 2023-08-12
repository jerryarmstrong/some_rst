tests/ui/derives/derives-span-Debug-struct.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-deriving-span-tests.py'


struct Error;

#[derive(Debug)]
struct Struct {
    x: Error //~ ERROR
}

fn main() {}


