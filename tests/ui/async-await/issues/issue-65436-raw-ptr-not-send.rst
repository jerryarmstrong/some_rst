tests/ui/async-await/issues/issue-65436-raw-ptr-not-send.rs
===========================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // edition:2018
// revisions: no_drop_tracking drop_tracking
// [drop_tracking] check-pass
// [drop_tracking] compile-flags: -Zdrop-tracking=yes
// [no_drop_tracking] compile-flags: -Zdrop-tracking=no

struct Foo(*const u8);

unsafe impl Send for Foo {}

async fn bar(_: Foo) {}

fn assert_send<T: Send>(_: T) {}

fn main() {
    assert_send(async {
        //[no_drop_tracking]~^ ERROR future cannot be sent between threads safely
        bar(Foo(std::ptr::null())).await;
    })
}


