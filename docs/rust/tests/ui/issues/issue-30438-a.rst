tests/ui/issues/issue-30438-a.rs
================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Original regression test for Issue #30438.

use std::ops::Index;

struct Test<'a> {
    s: &'a String
}

impl <'a> Index<usize> for Test<'a> {
    type Output = Test<'a>;
    fn index(&self, _: usize) -> &Self::Output {
        return &Test { s: &self.s};
        //~^ ERROR: cannot return reference to temporary value
    }
}

fn main() {
    let s = "Hello World".to_string();
    let test = Test{s: &s};
    let r = &test[0];
    println!("{}", test.s); // OK since test is valid
    println!("{}", r.s); // Segfault since value pointed by r has already been dropped
}


