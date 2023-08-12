tests/ui/borrowck/borrowck-mut-vec-as-imm-slice.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn want_slice(v: &[isize]) -> isize {
    let mut sum = 0;
    for i in v { sum += *i; }
    sum
}

fn has_mut_vec(v: Vec<isize> ) -> isize {
    want_slice(&v)
}

pub fn main() {
    assert_eq!(has_mut_vec(vec![1, 2, 3]), 6);
}


