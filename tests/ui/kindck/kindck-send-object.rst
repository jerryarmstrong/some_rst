tests/ui/kindck/kindck-send-object.rs
=====================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // Test which of the builtin types are considered sendable. The tests
// in this file all test the "kind" violates detected during kindck.
// See all `regions-bounded-by-send.rs`

fn assert_send<T:Send>() { }
trait Dummy { }
trait Message : Send { }

// careful with object types, who knows what they close over...

fn object_ref_with_static_bound_not_ok() {
    assert_send::<&'static (dyn Dummy + 'static)>();
    //~^ ERROR `(dyn Dummy + 'static)` cannot be shared between threads safely [E0277]
}

fn box_object_with_no_bound_not_ok<'a>() {
    assert_send::<Box<dyn Dummy>>();
    //~^ ERROR `dyn Dummy` cannot be sent between threads safely
}

fn object_with_send_bound_ok() {
    assert_send::<&'static (dyn Dummy + Sync)>();
    assert_send::<Box<dyn Dummy + Send>>();
}

fn main() { }


