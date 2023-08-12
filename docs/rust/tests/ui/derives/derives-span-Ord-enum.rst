tests/ui/derives/derives-span-Ord-enum.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // This file was auto-generated using 'src/etc/generate-deriving-span-tests.py'

#[derive(Eq,PartialOrd,PartialEq)]
struct Error;

#[derive(Ord,Eq,PartialOrd,PartialEq)]
enum Enum {
   A(
     Error //~ ERROR
     )
}

fn main() {}


