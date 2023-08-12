tests/ui/issues/auxiliary/issue-2170-lib.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    fn foo(_x: i32) {
}

pub struct rsrc {
  x: i32,
}

impl Drop for rsrc {
    fn drop(&mut self) {
        foo(self.x);
    }
}

pub fn rsrc(x: i32) -> rsrc {
    rsrc {
        x: x
    }
}


