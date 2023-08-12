tests/ui/closures/2229_closure_analysis/run_pass/by_value.rs
============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// run-pass

// Test that ByValue captures compile successfully especially when the captures are
// dereferenced within the closure.

#[derive(Debug, Default)]
struct SomeLargeType;
struct MuchLargerType([SomeLargeType; 32]);

fn big_box() {
    let s = MuchLargerType(Default::default());
    let b = Box::new(s);
    let t = (b, 10);

    let c = || {
        let p = t.0.0;
        println!("{} {:?}", t.1, p);
    };

    c();
}

fn main() {
    big_box();
}


