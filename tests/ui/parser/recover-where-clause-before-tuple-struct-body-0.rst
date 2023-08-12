tests/ui/parser/recover-where-clause-before-tuple-struct-body-0.rs
==================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issues #100790 and #106439.
// run-rustfix

pub struct Example
where
    (): Sized,
(usize);
//~^^^ ERROR where clauses are not allowed before tuple struct bodies

struct _Demo
where
    (): Sized,
    String: Clone,
(pub usize, usize);
//~^^^^ ERROR where clauses are not allowed before tuple struct bodies

fn main() {}


