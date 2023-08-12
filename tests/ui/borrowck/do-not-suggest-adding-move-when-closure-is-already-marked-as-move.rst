tests/ui/borrowck/do-not-suggest-adding-move-when-closure-is-already-marked-as-move.rs
======================================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn main() {
    let mut vec: Vec<i32> = Vec::new();
    let closure = move || {
        vec.clear();
        let mut iter = vec.iter();
        move || { iter.next() } //~ ERROR captured variable cannot escape `FnMut` closure bod
    };
}


