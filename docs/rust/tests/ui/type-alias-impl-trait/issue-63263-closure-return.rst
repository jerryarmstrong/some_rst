tests/ui/type-alias-impl-trait/issue-63263-closure-return.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #63263.
// Tests that we properly handle closures with an explicit return type
// that return an opaque type.

// check-pass

#![feature(type_alias_impl_trait)]

pub type Closure = impl FnOnce();

fn main() {
    || -> Closure { || () };
}


