tests/ui/closures/2229_closure_analysis/run_pass/fru_syntax.rs
==============================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
// run-pass

// Test that functional record update/struct update syntax works inside
// a closure when the feature `capture_disjoint_fields` is enabled.

#[derive(Clone)]
struct S {
    a: String,
    b: String,
}

struct T {
    a: String,
    s: S,
}

fn main() {
    let a = String::new();
    let b = String::new();
    let c = String::new();
    let s = S {a, b};
    let t = T {
        a: c,
        s: s.clone()
    };

    let c = || {
        let s2 = S {
            a: format!("New s2"),
            ..s
        };
        let s3 = S {
            a: format!("New s3"),
            ..t.s
        };
        println!("{} {}", s2.a, s2.b);
        println!("{} {} {}", s3.a, s3.b, t.a);
    };

    c();
}


