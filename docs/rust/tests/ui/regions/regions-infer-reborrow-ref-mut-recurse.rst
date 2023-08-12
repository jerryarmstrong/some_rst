tests/ui/regions/regions-infer-reborrow-ref-mut-recurse.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
// Test an edge case in region inference: the lifetime of the borrow
// of `*x` must be extended to at least 'a.

// pretty-expanded FIXME #23616

fn foo<'a,'b>(x: &'a &'b mut isize) -> &'a isize {
    let y = &*x; // should be inferred to have type &'a &'b mut isize...

    // ...because if we inferred, say, &'x &'b mut isize where 'x <= 'a,
    // this reborrow would be illegal:
    &**y
}

pub fn main() {
    /* Just want to know that it compiles. */
}


