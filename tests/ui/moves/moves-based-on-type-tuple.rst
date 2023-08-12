tests/ui/moves/moves-based-on-type-tuple.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn dup(x: Box<isize>) -> Box<(Box<isize>,Box<isize>)> {


    Box::new((x, x))
    //~^ use of moved value: `x` [E0382]
}

fn main() {
    dup(Box::new(3));
}


