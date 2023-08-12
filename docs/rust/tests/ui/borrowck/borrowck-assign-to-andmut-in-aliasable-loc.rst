tests/ui/borrowck/borrowck-assign-to-andmut-in-aliasable-loc.rs
===============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that assignments to an `&mut` pointer which is found in a
// borrowed (but otherwise non-aliasable) location is illegal.

struct S<'a> {
    pointer: &'a mut isize
}

fn a(s: &S) {
    *s.pointer += 1; //~ ERROR cannot assign
}

fn b(s: &mut S) {
    *s.pointer += 1;
}

fn c(s: & &mut S) {
    *s.pointer += 1; //~ ERROR cannot assign
}

fn main() {}


