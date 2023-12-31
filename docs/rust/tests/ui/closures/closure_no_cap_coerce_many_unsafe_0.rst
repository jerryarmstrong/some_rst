tests/ui/closures/closure_no_cap_coerce_many_unsafe_0.rs
========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // revisions: mir thir
// [thir]compile-flags: -Z thir-unsafeck

// Ensure we get unsafe function after coercion
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
    let result: i32 = foo(5, 5); //~ ERROR call to unsafe function


    // We can coerce unsafe function to non-capturing closure
    let foo = match "+" {
        "-" => |a, b| (a - b) as i32,
        "+" => add,
        _ => unimplemented!(),
    };
    let result: i32 = foo(5, 5); //~ ERROR call to unsafe function
}


