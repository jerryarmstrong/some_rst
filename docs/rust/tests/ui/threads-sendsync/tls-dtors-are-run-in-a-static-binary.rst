tests/ui/threads-sendsync/tls-dtors-are-run-in-a-static-binary.rs
=================================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // run-pass
// no-prefer-dynamic
// ignore-emscripten no threads support

static mut HIT: bool = false;

struct Foo;

impl Drop for Foo {
    fn drop(&mut self) {
        unsafe { HIT = true; }
    }
}

thread_local!(static FOO: Foo = Foo);

fn main() {
    std::thread::spawn(|| {
        FOO.with(|_| {});
    }).join().unwrap();
    assert!(unsafe { HIT });
}


