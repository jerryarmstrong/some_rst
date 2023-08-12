tests/ui/variance/variance-use-contravariant-struct-2.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test various uses of structs with distinct variances to make sure
// they permit lifetimes to be approximated as expected.

#![allow(dead_code)]
// build-pass (FIXME(62277): could be check-pass?)

struct SomeStruct<T>(fn(T));

fn bar<'min,'max>(v: SomeStruct<&'min ()>)
                  -> SomeStruct<&'max ()>
    where 'max : 'min
{
    v
}


fn main() { }


