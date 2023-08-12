tests/ui/nll/guarantor-issue-46974.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that NLL analysis propagates lifetimes correctly through
// field accesses, Box accesses, etc.

fn foo(s: &mut (i32,)) -> i32 {
    let t = &mut *s; // this borrow should last for the entire function
    let x = &t.0;
    *s = (2,); //~ ERROR cannot assign to `*s`
    *x
}

fn bar(s: &Box<(i32,)>) -> &'static i32 {
    // FIXME(#46983): error message should be better
    &s.0 //~ ERROR lifetime may not live long enough
}

fn main() {
    foo(&mut (0,));
    bar(&Box::new((1,)));
}


