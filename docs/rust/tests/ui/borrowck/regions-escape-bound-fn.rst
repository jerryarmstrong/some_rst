tests/ui/borrowck/regions-escape-bound-fn.rs
============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn with_int<F>(f: F)
where
    F: FnOnce(&isize),
{
    let x = 3;
    f(&x);
}

fn main() {
    let mut x: Option<&isize> = None;
    with_int(|y| x = Some(y));
    //~^ ERROR borrowed data escapes outside of closure
}


