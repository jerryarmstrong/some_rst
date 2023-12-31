tests/mir-opt/inline/inline_cycle_generic.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that inliner handles various forms of recursion and doesn't fall into
// an infinite inlining cycle. The particular outcome of inlining is not
// crucial otherwise.
//
// Regression test for issue #78573.

// EMIT_MIR inline_cycle_generic.main.Inline.diff
fn main() {
    <C as Call>::call();
}

pub trait Call {
    fn call();
}

pub struct A;
pub struct B<T>(T);
pub struct C;

impl Call for A {
    #[inline]
    fn call() {
        <B<C> as Call>::call()
    }
}


impl<T: Call> Call for B<T> {
    #[inline]
    fn call() {
        <T as Call>::call()
    }
}

impl Call for C {
    #[inline]
    fn call() {
        <B<A> as Call>::call()
    }
}


