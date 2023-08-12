tests/ui/regions/regions-infer-borrow-scope-view.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn view<T>(x: &[T]) -> &[T] {x}

pub fn main() {
    let v = vec![1, 2, 3];
    let x = view(&v);
    let y = view(x);
    assert!((v[0] == x[0]) && (v[0] == y[0]));
}


