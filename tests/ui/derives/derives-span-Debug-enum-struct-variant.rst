tests/ui/derives/derives-span-Debug-enum-struct-variant.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-deriving-span-tests.py'


struct Error;

#[derive(Debug)]
enum Enum {
   A {
     x: Error //~ ERROR
   }
}

fn main() {}


