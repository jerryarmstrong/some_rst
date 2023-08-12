tests/ui/regions/regions-return-ref-to-upvar-issue-17403.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that closures cannot subvert aliasing restrictions

fn main() {
    // Unboxed closure case
    {
        let mut x = 0;
        let mut f = || &mut x; //~ ERROR captured variable cannot escape `FnMut` closure body
        let x = f();
        let y = f();
    }
}


