tests/ui/borrowck/borrowck-while-break.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn test(cond: bool) {
    let v;
    while cond {
        v = 3;
        break;
    }
    println!("{}", v); //~ ERROR E0381
}

fn main() {
    test(true);
}


