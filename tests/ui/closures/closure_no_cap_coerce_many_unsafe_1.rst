tests/ui/closures/closure_no_cap_coerce_many_unsafe_1.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// Ensure we get correct unsafe function after coercion
unsafe fn add(a: i32, b: i32) -> i32 {
    a + b
}
fn main() {
    // We can coerce non-capturing closure to unsafe function
    let foo = match "+" {
        "+" => add,
        "-" => |a, b| (a - b) as i32,
        _ => unimplemented!(),
    };
    assert_eq!(unsafe { foo(5, 5) }, 10);


    // We can coerce unsafe function to non-capturing closure
    let foo = match "-" {
        "-" => |a, b| (a - b) as i32,
        "+" => add,
        _ => unimplemented!(),
    };
    assert_eq!(unsafe { foo(5, 5) }, 0);
}


