tests/ui/lifetimes/issue-70917-lifetimes-in-fn-def.rs
=====================================================

Last edited: 2023-03-30 20:35:59

Contents:

.. code-block:: rs

    // check-pass

fn assert_static<T: 'static>(_: T) {}

// NOTE(eddyb) the `'a: 'a` may look a bit strange, but we *really* want
// `'a` to be an *early-bound* parameter, otherwise it doesn't matter anyway.
fn capture_lifetime<'a: 'a>() {}

fn test_lifetime<'a>() {
    assert_static(capture_lifetime::<'a>);
}

fn main() {}


