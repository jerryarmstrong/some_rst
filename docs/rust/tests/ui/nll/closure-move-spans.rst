tests/ui/nll/closure-move-spans.rs
==================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check that moves due to a closure capture give a special note

fn move_after_move(x: String) {
    || x;
    let y = x; //~ ERROR
}

fn borrow_after_move(x: String) {
    || x;
    let y = &x; //~ ERROR
}

fn borrow_mut_after_move(mut x: String) {
    || x;
    let y = &mut x; //~ ERROR
}

fn fn_ref<F: Fn()>(f: F) -> F { f }
fn fn_mut<F: FnMut()>(f: F) -> F { f }

fn main() {}


