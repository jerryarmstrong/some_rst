tests/ui/function-pointer/function-pointer-comparison-issue-54685.rs
====================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // compile-flags: -C opt-level=3
// run-pass

fn foo(_i: i32) -> i32 {
    1
}
fn bar(_i: i32) -> i32 {
    1
}

fn main() {
    let x: fn(i32) -> i32 = foo;
    let y: fn(i32) -> i32 = bar;

    let s1;
    if x == y {
        s1 = "same".to_string();
    } else {
        s1 = format!("{:?}, {:?}", x, y);
    }

    let s2;
    if x == y {
        s2 = "same".to_string();
    } else {
        s2 = format!("{:?}, {:?}", x, y);
    }

    assert_eq!(s1, s2);
}


