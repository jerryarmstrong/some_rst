tests/ui/borrowck/regions-escape-unboxed-closure.rs
===================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn with_int(f: &mut dyn FnMut(&isize)) {}

fn main() {
    let mut x: Option<&isize> = None;
    with_int(&mut |y| x = Some(y));
    //~^ ERROR borrowed data escapes outside of closure
}


