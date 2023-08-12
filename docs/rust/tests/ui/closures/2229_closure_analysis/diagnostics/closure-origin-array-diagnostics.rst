tests/ui/closures/2229_closure_analysis/diagnostics/closure-origin-array-diagnostics.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

// Test that array access is not stored as part of closure kind origin

fn expect_fn<F: Fn()>(_f: F) {}

fn main() {
    let s = [format!("s"), format!("s")];
    let c = || { //~ ERROR expected a closure that implements the `Fn`
        let [_, _s] = s;
    };
    expect_fn(c);
}


