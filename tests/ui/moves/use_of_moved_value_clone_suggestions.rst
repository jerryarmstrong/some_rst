tests/ui/moves/use_of_moved_value_clone_suggestions.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // `Rc` is not ever `Copy`, we should not suggest adding `T: Copy` constraint
fn duplicate_rc<T>(t: std::rc::Rc<T>) -> (std::rc::Rc<T>, std::rc::Rc<T>) {
    (t, t) //~ use of moved value: `t`
}

fn main() {}


