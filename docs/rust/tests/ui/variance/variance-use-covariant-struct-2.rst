tests/ui/variance/variance-use-covariant-struct-2.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a covariant struct permits the lifetime of a reference to
// be shortened.

#![allow(dead_code)]
// build-pass (FIXME(62277): could be check-pass?)

struct SomeStruct<T>(T);

fn foo<'min,'max>(v: SomeStruct<&'max ()>)
                  -> SomeStruct<&'min ()>
    where 'max : 'min
{
    v
}

fn main() { }


