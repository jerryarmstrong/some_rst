tests/ui/generics/generic-fn-twice.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass



// pretty-expanded FIXME #23616

mod foomod {
    pub fn foo<T>() { }
}

pub fn main() { foomod::foo::<isize>(); foomod::foo::<isize>(); }


