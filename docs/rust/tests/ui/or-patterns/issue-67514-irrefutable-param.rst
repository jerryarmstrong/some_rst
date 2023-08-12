tests/ui/or-patterns/issue-67514-irrefutable-param.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Check that we don't ICE for irrefutable or-patterns in function parameters

// check-pass

fn foo((Some(_) | None): Option<u32>) {}

fn main() {
    foo(None);
}


