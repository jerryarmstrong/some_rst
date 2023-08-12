tests/ui/nll/return-ref-mut-issue-46557.rs
==========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Regression test for issue #46557

fn gimme_static_mut() -> &'static mut u32 {
    let ref mut x = 1234543;
    x //~ ERROR cannot return value referencing temporary value [E0515]
}

fn main() {}


