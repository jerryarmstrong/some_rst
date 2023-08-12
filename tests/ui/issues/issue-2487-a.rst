tests/ui/issues/issue-2487-a.rs
===============================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // build-pass
#![allow(dead_code)]
#![allow(non_camel_case_types)]

// pretty-expanded FIXME #23616

struct socket {
    sock: isize,

}

impl Drop for socket {
    fn drop(&mut self) {}
}

impl socket {
    pub fn set_identity(&self)  {
        closure(|| setsockopt_bytes(self.sock.clone()))
    }
}

fn socket() -> socket {
    socket {
        sock: 1
    }
}

fn closure<F>(f: F) where F: FnOnce() { f() }

fn setsockopt_bytes(_sock: isize) { }

pub fn main() {}


