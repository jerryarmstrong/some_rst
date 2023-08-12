tests/ui/borrowck/borrowck-move-moved-value-into-closure.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn call_f<F:FnOnce() -> isize>(f: F) -> isize {
    f()
}



fn main() {
    let t: Box<_> = Box::new(3);

    call_f(move|| { *t + 1 });
    call_f(move|| { *t + 1 }); //~ ERROR use of moved value
}


