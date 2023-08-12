tests/ui/inference/question-mark-type-infer.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test that type inference fails where there are multiple possible return types
// for the `?` operator.

fn f(x: &i32) -> Result<i32, ()> {
    Ok(*x)
}

fn g() -> Result<Vec<i32>, ()> {
    let l = [1, 2, 3, 4];
    l.iter().map(f).collect()?
    //~^ ERROR type annotations needed
}

fn main() {
    g();
}


