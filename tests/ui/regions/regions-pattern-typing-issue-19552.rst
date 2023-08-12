tests/ui/regions/regions-pattern-typing-issue-19552.rs
======================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn assert_static<T: 'static>(_t: T) {}

fn main() {
    let line = String::new();
    match [&*line] { //~ ERROR `line` does not live long enough
        [ word ] => { assert_static(word); }
    }
}


