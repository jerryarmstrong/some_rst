tests/ui/array-slice-vec/mutable-alias-vec.rs
=============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass

fn grow(v: &mut Vec<isize> ) {
    v.push(1);
}

pub fn main() {
    let mut v: Vec<isize> = Vec::new();
    grow(&mut v);
    grow(&mut v);
    grow(&mut v);
    let len = v.len();
    println!("{}", len);
    assert_eq!(len, 3 as usize);
}


