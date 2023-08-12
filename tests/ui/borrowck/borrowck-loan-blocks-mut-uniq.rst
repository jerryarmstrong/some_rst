tests/ui/borrowck/borrowck-loan-blocks-mut-uniq.rs
==================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn borrow<F>(v: &isize, f: F) where F: FnOnce(&isize) {
    f(v);
}



fn box_imm() {
    let mut v: Box<_> = Box::new(3);
    borrow(&*v,
           |w| { //~ ERROR cannot borrow `v` as mutable
            v = Box::new(4);
            assert_eq!(*v, 3);
            assert_eq!(*w, 4);
        })
}

fn main() {
}


