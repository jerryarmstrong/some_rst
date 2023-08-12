tests/ui/type/type-check/point-at-inference-2.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bar(_: Vec<i32>) {}
fn baz(_: &Vec<&i32>) {}
fn main() {
    let v = vec![&1];
    bar(v); //~ ERROR E0308
    let v = vec![];
    baz(&v);
    baz(&v);
    bar(v); //~ ERROR E0308
    let v = vec![];
    baz(&v);
    bar(v); //~ ERROR E0308
}


