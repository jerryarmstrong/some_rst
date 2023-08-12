tests/ui/closures/2229_closure_analysis/run_pass/capture_with_wildcard_match.rs
===============================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2021
//check-pass

fn test1() {
    let foo : [Vec<u8>; 3] = ["String".into(), "String".into(), "String".into()];
    let c = || {
        match foo { _ => () };
    };
    drop(foo);
    c();
}

fn test2() {
    let foo : Option<[Vec<u8>; 3]> = Some(["String".into(), "String".into(), "String".into()]);
    let c = || {
        match foo {
            Some(_) => 1,
            _ => 2
        };
    };
    c();
}

fn main() {
    test1();
    test2();
}


