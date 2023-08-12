tests/ui/borrowck/borrowck-ref-mut-of-imm.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn destructure(x: Option<isize>) -> isize {
    match x {
      None => 0,
      Some(ref mut v) => *v //~ ERROR cannot borrow
    }
}

fn main() {
    assert_eq!(destructure(Some(22)), 22);
}


