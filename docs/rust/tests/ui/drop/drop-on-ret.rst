tests/ui/drop/drop-on-ret.rs
============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass



// pretty-expanded FIXME #23616

fn f() -> isize {
    if true {
        let _s: String = "should not leak".to_string();
        return 1;
    }
    return 0;
}

pub fn main() { f(); }


