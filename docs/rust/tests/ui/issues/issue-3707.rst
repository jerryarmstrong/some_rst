tests/ui/issues/issue-3707.rs
=============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    struct Obj {
    member: usize
}

impl Obj {
    pub fn boom() -> bool {
        return 1+1 == 2
    }
    pub fn chirp(&self) {
        self.boom(); //~ ERROR no method named `boom` found
    }
}

fn main() {
    let o = Obj { member: 0 };
    o.chirp();
    1 + 1;
}


