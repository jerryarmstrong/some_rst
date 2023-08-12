tests/ui/borrowck/borrowck-mut-addr-of-imm-var.rs
=================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: isize = 3;
    let y: &mut isize = &mut x; //~ ERROR cannot borrow
    *y = 5;
    println!("{}", *y);
}


