tests/ui/moves/issue-99470-move-out-of-some.rs
==============================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let x: &Option<Box<i32>> = &Some(Box::new(0));

    match x {
    //~^ ERROR cannot move out of `x` as enum variant `Some` which is behind a shared reference
        &Some(_y) => (),
        &None => (),
    }
}


