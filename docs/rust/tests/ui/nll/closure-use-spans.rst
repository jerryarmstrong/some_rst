tests/ui/nll/closure-use-spans.rs
=================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that liveness due to a closure capture gives a special note

fn use_as_borrow_capture(mut x: i32) {
    let y = &x;
    x = 0; //~ ERROR
    || *y;
}

fn use_as_borrow_mut_capture(mut x: i32) {
    let y = &mut x;
    x = 0; //~ ERROR
    || *y = 1;
}

fn use_as_move_capture(mut x: i32) {
    let y = &x;
    x = 0; //~ ERROR
    move || *y;
}

fn main() {}


