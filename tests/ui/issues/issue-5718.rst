tests/ui/issues/issue-5718.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// pretty-expanded FIXME #23616

struct Element;

macro_rules! foo {
    ($tag: expr, $string: expr) => {
        if $tag == $string {
            let element: Box<_> = Box::new(Element);
            unsafe {
                return std::mem::transmute::<_, usize>(element);
            }
        }
    }
}

fn bar() -> usize {
    foo!("a", "b");
    0
}

fn main() {
    bar();
}


