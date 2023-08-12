tests/ui/borrowck/borrowck-unboxed-closures.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn a<F:Fn(isize, isize) -> isize>(mut f: F) {
    let g = &mut f;
    f(1, 2);    //~ ERROR cannot borrow `f` as immutable
    use_mut(g);
}
fn b<F:FnMut(isize, isize) -> isize>(f: F) {
    f(1, 2);    //~ ERROR cannot borrow `f` as mutable, as it is not declared as mutable
}

fn c<F:FnOnce(isize, isize) -> isize>(f: F) {
    f(1, 2);
    f(1, 2);    //~ ERROR use of moved value
}

fn main() {}

fn use_mut<T>(_: &mut T) { }


