tests/ui/mir/mir_early_return_scope.rs
======================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
#![allow(unused_variables)]
static mut DROP: bool = false;

struct ConnWrap(Conn);
impl ::std::ops::Deref for ConnWrap {
    type Target=Conn;
    fn deref(&self) -> &Conn { &self.0 }
}

struct Conn;
impl Drop for  Conn {
    fn drop(&mut self) { unsafe { DROP = true; } }
}

fn inner() {
    let conn = &*match Some(ConnWrap(Conn)) {
        Some(val) => val,
        None => return,
    };
    return;
}

fn main() {
    inner();
    unsafe {
        assert_eq!(DROP, true);
    }
}


