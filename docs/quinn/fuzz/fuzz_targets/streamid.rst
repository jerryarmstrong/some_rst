fuzz/fuzz_targets/streamid.rs
=============================

Last edited: 2022-02-11 21:48:07

Contents:

.. code-block:: rs

    #![no_main]
use arbitrary::Arbitrary;
use libfuzzer_sys::fuzz_target;

extern crate proto;
use proto::{Dir, Side, StreamId};

#[derive(Arbitrary, Debug)]
struct StreamIdParams {
    side: Side,
    dir: Dir,
    index: u64,
}

fuzz_target!(|data: StreamIdParams| {
    let s = StreamId::new(data.side, data.dir, data.index);
    assert_eq!(s.initiator(), data.side);
    assert_eq!(s.dir(), data.dir);
});


