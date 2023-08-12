tests/ui/type/type-check/point-at-inference.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn bar(_: Vec<i32>) {}
fn baz(_: &impl std::any::Any) {}
fn main() {
    let v = vec![1, 2, 3, 4, 5];
    let mut foo = vec![];
    baz(&foo);
    for i in &v {
        foo.push(i);
    }
    baz(&foo);
    bar(foo); //~ ERROR E0308
}


