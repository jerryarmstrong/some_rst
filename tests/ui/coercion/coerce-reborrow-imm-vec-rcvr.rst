tests/ui/coercion/coerce-reborrow-imm-vec-rcvr.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass


fn bar(v: &mut [usize]) -> Vec<usize> {
    v.to_vec()
}

fn bip(v: &[usize]) -> Vec<usize> {
    v.to_vec()
}

pub fn main() {
    let mut the_vec = vec![1, 2, 3, 100];
    assert_eq!(the_vec.clone(), bar(&mut the_vec));
    assert_eq!(the_vec.clone(), bip(&the_vec));
}


