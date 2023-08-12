tests/ui/typeck/issue-72225-call-fnmut-through-derefmut.rs
==========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

// rust-lang/rust#72225: confusing diagnostics when calling FnMut through DerefMut.

use std::cell::RefCell;

struct S {
    f: Box<dyn FnMut()>
}

fn test(s: &RefCell<S>) {
    let mut guard = s.borrow_mut();
    (guard.f)();
}

fn main() {
    let s = RefCell::new(S {
        f: Box::new(|| ())
    });
    test(&s);
}


