tests/ui/trivial-bounds/trivial-bounds-object.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Check that the object bound dyn A + 'a: A is preferred over the
// where clause bound dyn A + 'static: A.

#![allow(unused)]

trait A {
    fn test(&self);
}

fn foo(x: &dyn A)
where
    dyn A + 'static: A, // Using this bound would lead to a lifetime error.
{
    x.test();
}

fn main () {}


