tests/ui/issues/auxiliary/issue-3136-a.rs
=========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    trait x {
    fn use_x<T>(&self);
}
struct y(());
impl x for y {
    fn use_x<T>(&self) {
        struct foo { //~ ERROR quux
            i: ()
        }
        fn new_foo<T>(i: ()) -> foo {
            foo { i: i }
        }
    }
}


