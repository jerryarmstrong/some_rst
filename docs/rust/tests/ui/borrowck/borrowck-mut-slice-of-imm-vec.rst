tests/ui/borrowck/borrowck-mut-slice-of-imm-vec.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn write(v: &mut [isize]) {
    v[0] += 1;
}

fn main() {
    let v = vec![1, 2, 3];
    write(&mut v); //~ ERROR cannot borrow
}


