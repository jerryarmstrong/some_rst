tests/ui/threads-sendsync/sendfn-spawn-with-fn-arg.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// ignore-emscripten no threads support

use std::thread;

pub fn main() { test05(); }

fn test05_start<F:FnOnce(isize)>(f: F) {
    f(22);
}

fn test05() {
    let three: Box<_> = Box::new(3);
    let fn_to_send = move|n:isize| {
        println!("{}", *three + n); // will copy x into the closure
        assert_eq!(*three, 3);
    };
    thread::spawn(move|| {
        test05_start(fn_to_send);
    }).join().ok().unwrap();
}


