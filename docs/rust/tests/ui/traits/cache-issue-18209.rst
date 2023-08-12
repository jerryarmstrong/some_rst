tests/ui/traits/cache-issue-18209.rs
====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Test that the cache results from the default method do not pollute
// the cache for the later call in `load()`.
//
// See issue #18209.

// pretty-expanded FIXME #23616

pub trait Foo {
    fn load_from() -> Box<Self>;
    fn load() -> Box<Self> {
        Foo::load_from()
    }
}

pub fn load<M: Foo>() -> Box<M> {
    Foo::load()
}

fn main() { }


