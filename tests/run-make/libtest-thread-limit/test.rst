tests/run-make/libtest-thread-limit/test.rs
===========================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    #![feature(once_cell)]

use std::{
    io::ErrorKind,
    sync::OnceLock,
    thread::{self, Builder, ThreadId},
};

static THREAD_ID: OnceLock<ThreadId> = OnceLock::new();

#[test]
fn spawn_thread_would_block() {
    assert_eq!(Builder::new().spawn(|| unreachable!()).unwrap_err().kind(), ErrorKind::WouldBlock);
    THREAD_ID.set(thread::current().id()).unwrap();
}

#[test]
fn run_in_same_thread() {
    assert_eq!(*THREAD_ID.get().unwrap(), thread::current().id());
}


