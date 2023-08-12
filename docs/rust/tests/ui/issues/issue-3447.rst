tests/ui/issues/issue-3447.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(dead_code)]
#![allow(non_snake_case)]
#![allow(non_camel_case_types)]

use std::cell::RefCell;

static S: &'static str = "str";

struct list<T> {
    element: T,
    next: Option<Box<RefCell<list<T>>>>
}

impl<T:'static> list<T> {
    pub fn addEnd(&mut self, element: T) {
        let newList = list {
            element: element,
            next: None
        };

        self.next = Some(Box::new(RefCell::new(newList)));
    }
}

pub fn main() {
    let ls = list {
        element: S,
        next: None
    };
    println!("{}", ls.element);
}


