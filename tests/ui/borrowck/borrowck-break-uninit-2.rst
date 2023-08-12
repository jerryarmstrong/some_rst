tests/ui/borrowck/borrowck-break-uninit-2.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo() -> isize {
    let x: isize;

    while 1 != 2  {
        break;
        x = 0;
    }

    println!("{}", x); //~ ERROR E0381

    return 17;
}

fn main() { println!("{}", foo()); }


