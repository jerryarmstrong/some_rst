tests/ui/closures/2229_closure_analysis/diagnostics/closure-origin-tuple-diagnostics-1.rs
=========================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

// Check that precise paths are being reported back in the error message.

fn main() {
    let mut x = (5, 0);
    let hello = || {
        x.0 += 1;
    };

    let b = hello;
    let c = hello; //~ ERROR use of moved value: `hello` [E0382]
}


