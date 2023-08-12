tests/ui/variance/variance-object-types.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(rustc_attrs)]


// For better or worse, associated types are invariant, and hence we
// get an invariant result for `'a`.
#[rustc_variance]
struct Foo<'a> { //~ ERROR [o]
    x: Box<dyn Fn(i32) -> &'a i32 + 'static>
}

fn main() {
}


