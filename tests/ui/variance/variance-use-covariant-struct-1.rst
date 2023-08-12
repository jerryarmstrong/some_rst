tests/ui/variance/variance-use-covariant-struct-1.rs
====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that a covariant struct does not permit the lifetime of a
// reference to be enlarged.

struct SomeStruct<T>(T);

fn foo<'min,'max>(v: SomeStruct<&'min ()>)
                  -> SomeStruct<&'max ()>
    where 'max : 'min
{
    v
    //~^ ERROR lifetime may not live long enough
}

fn main() { }


