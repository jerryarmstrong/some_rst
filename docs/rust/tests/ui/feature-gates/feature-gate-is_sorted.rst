tests/ui/feature-gates/feature-gate-is_sorted.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    // Assert `Iterator` methods are unstable
    assert!([1, 2, 2, 9].iter().is_sorted());
    //~^ ERROR: use of unstable library feature 'is_sorted': new API
    assert!(![-2i32, -1, 0, 3].iter().is_sorted_by_key(|n| n.abs()));
    //~^ ERROR: use of unstable library feature 'is_sorted': new API

    // Assert `[T]` methods are unstable
    assert!([1, 2, 2, 9].is_sorted());
    //~^ ERROR: use of unstable library feature 'is_sorted': new API
    assert!(![-2i32, -1, 0, 3].is_sorted_by_key(|n| n.abs()));
    //~^ ERROR: use of unstable library feature 'is_sorted': new API
}


