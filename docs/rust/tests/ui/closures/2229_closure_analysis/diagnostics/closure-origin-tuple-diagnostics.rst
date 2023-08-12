tests/ui/closures/2229_closure_analysis/diagnostics/closure-origin-tuple-diagnostics.rs
=======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021

struct S(String, String);

fn expect_fn<F: Fn()>(_f: F) {}

fn main() {
    let s = S(format!("s"), format!("s"));
    let c = || { //~ ERROR expected a closure that implements the `Fn`
        let s = s.1;
    };
    expect_fn(c);
}


