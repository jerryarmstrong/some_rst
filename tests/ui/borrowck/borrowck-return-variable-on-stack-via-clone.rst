tests/ui/borrowck/borrowck-return-variable-on-stack-via-clone.rs
================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that when we clone a `&T` pointer we properly relate the
// lifetime of the pointer which results to the pointer being cloned.
// Bugs in method resolution have sometimes broken this connection.
// Issue #19261.

fn leak<'a, T>(x: T) -> &'a T {
    (&x).clone() //~ ERROR cannot return value referencing function parameter `x`
}

fn main() { }


