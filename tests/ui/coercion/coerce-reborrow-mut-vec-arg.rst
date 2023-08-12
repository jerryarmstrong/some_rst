tests/ui/coercion/coerce-reborrow-mut-vec-arg.rs
================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn reverse(v: &mut [usize]) {
    v.reverse();
}

fn bar(v: &mut [usize]) {
    reverse(v);
    reverse(v);
    reverse(v);
}

pub fn main() {
    let mut the_vec = vec![1, 2, 3, 100];
    bar(&mut the_vec);
    assert_eq!(the_vec, [100, 3, 2, 1]);
}


